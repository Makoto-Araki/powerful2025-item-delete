import os
import csv
import requests
from dotenv import load_dotenv

# ===== トークン読み込み =====
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# ===== Shopify設定 =====
SHOPIFY_STORE = "powerful2025.myshopify.com"
API_VERSION = "2025-10"

# ===== GraphQLエンドポイントと共通ヘッダー =====
GRAPHQL_URL = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}/graphql.json"
HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": ACCESS_TOKEN
}

# ===== GraphQL 商品削除関数 =====
def delete_product_by_gid(product_gid: str):
    """GraphQL形式のGIDを使って商品削除"""
    query = """
    mutation productDelete($input: ProductDeleteInput!) {
      productDelete(input: $input) {
        deletedProductId
        userErrors {
          field
          message
        }
      }
    }
    """

    variables = {
        "input": {
            "id": product_gid
        }
    }

    response = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables}
    )

    if response.status_code != 200:
        print(f"❌ APIリクエスト失敗: {response.status_code} - {response.text}")
        return

    data = response.json()

    errors = data.get("data", {}).get("productDelete", {}).get("userErrors", [])
    deleted_id = data.get("data", {}).get("productDelete", {}).get("deletedProductId")

    if deleted_id:
        print(f"✅ 商品削除成功: {deleted_id}")
    elif errors:
        for e in errors:
            print(f"⚠️ 削除エラー: {e['message']}")
    else:
        print(f"❌ 不明なエラー: {data}")

# ===== メイン処理 =====
def main():
    input_folder = os.path.join(os.path.dirname(__file__), "input")
    csv_files = os.listdir(input_folder)

    if not csv_files:
        print("⚠️ inputフォルダ内にCSVファイルが見つかりません。")
        return

    for csv_file in csv_files:
        print(f"\n📄 処理中: {csv_file}")
        with open(os.path.join(input_folder, csv_file), newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product_gid = row.get("product_id")
                if product_gid:
                    delete_product_by_gid(product_gid.strip())
                else:
                    print(f"⚠️ CSV行にproduct_idがありません: {row}")

if __name__ == "__main__":
    main()
