import os
import csv
import requests
from dotenv import load_dotenv

# --- トークン読み込み ---
load_dotenv()
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

# --- Shopify設定 ---
SHOPIFY_STORE = "powerful2025.myshopify.com"
API_VERSION = "2025-10"

def register_product(title, price, inventory, image_url=None):
    url = f"https://{SHOPIFY_STORE}/admin/api/{API_VERSION}/products.json"
    headers = {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": ACCESS_TOKEN
    }
    
    product_payload = {
        "product": {
            "title": title,
            "variants": [
                {
                    "price": price,
                    "inventory_management": "shopify",
                    "inventory_quantity": inventory
                }
            ]
        }
    }
    
    # 画像URLがある場合は images フィールドを追加
    if image_url:
        product_payload["product"]["images"] = [{"src": image_url}]
    
    response = requests.post(url, json=product_payload, headers=headers)
    
    if response.status_code == 201:
        print(f"登録成功: {title}")
    else:
        print(f"登録失敗: {title} / {response.status_code} / {response.text}")

def main():
    input_folder = os.path.join(os.path.dirname(__file__), "input")
    
    # inputフォルダ内のすべてのCSVを処理
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".csv"):
            csv_path = os.path.join(input_folder, file_name)
            with open(csv_path, encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    title = row["title"]
                    price = row["price"]
                    inventory = int(row["inventory"])
                    image_url = row.get("image", None)  # 画像URL列がない場合はNone
                    register_product(title, price, inventory, image_url)

if __name__ == "__main__":
    main()
