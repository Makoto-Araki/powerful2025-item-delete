import os
import csv
import glob
import requests

# --- トークン読み込み ---
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# --- Shopify設定 ---
SHOPIFY_STORE = "powerful2025.myshopify.com"
API_VERSION = "2025-10"

# ===== ベースURLと共通ヘッダー =====
BASE_URL = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}"
HEADERS = {
    "Content-Type": "application/json",
    "X-Shopify-Access-Token": os.getenv('ACCESS_TOKEN')
}

# ===== 商品削除関数 =====
def delete_product_by_id(product_id: str):
    """商品IDを指定して削除"""
    url = f"{BASE_URL}/products/{product_id}.json"
    response = requests.delete(url, headers=HEADERS)
    if response.status_code == 200:
        print(f"✅ 商品ID {product_id} を削除しました。")
    elif response.status_code == 404:
        print(f"⚠️ 商品ID {product_id} が見つかりません。")
    else:
        print(f"❌ 商品ID {product_id} の削除に失敗: {response.status_code} - {response.text}")

# ===== メイン処理 =====
def main():
    input_folder = os.path.join(os.path.dirname(__file__), "input")
    csv_files = os.listdir(input_folder)

    if not csv_files:
        print("⚠️ inputフォルダ内にCSVファイルが見つかりません。")
        return

    for csv_file in csv_files:
        print(f"\n📄 処理中: {csv_file}")
        with open(csv_file, newline='', encoding='utf-8-sig') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product_id = row.get("id")
                handle = row.get("handle")

                if product_id:
                    delete_product_by_id(product_id.strip())
                elif handle:
                    pid = get_product_id_by_handle(handle.strip())
                    if pid:
                        delete_product_by_id(pid)
                    else:
                        print(f"⚠️ ハンドル {handle} に対応する商品が見つかりません。")
                else:
                    print(f"⚠️ CSV行にidまたはhandleがありません: {row}")


if __name__ == "__main__":
    main()
