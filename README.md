# powerful2025-item-insert (商品登録)

## 前提条件
- Shopifyに開発ストアpowerful2025が存在
- 開発ストアのAPIトークン作成済
- リモートリポジトリ作成済

## 処理概要
- inputフォルダ内の入力CSVファイルの商品情報を読み取り、開発ストアpowerful2025に登録

## 商品画像を管理画面に登録
### Shopify管理画面
#### 手順01
![管理画面操作01](images/content_upload_01.png)
#### 手順02
![管理画面操作02](images/content_upload_02.png)
#### 手順03
![管理画面操作03](images/content_upload_03.png)
#### 手順04
![管理画面操作04](images/content_upload_04.png)
#### 手順05
![管理画面操作05](images/content_upload_05.png)
#### 手順06
![管理画面操作06](images/content_upload_06.png)
#### 手順07
- クリックボードに画像URLがコピー

## 入力CSVファイルのサンプル
![入力CSVファイルサンプル01](images/input_csv_01.png)

## 環境構築
### ローカルリポジトリ作成
```bash
## パッケージ更新
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install python3-venv -y

## ディレクトリ移動
$ mkdir ~/powerful2025-item-register
$ cd powerful2025-item-register

## ローカルリポジトリ初期化
$ git init
$ git config --global user.email (自分のメールアドレス)
$ git config --global user.name Makoto-Araki

## リモートリポジトリ設定
$ git branch -M main
$ git remote add origin git@github.com:Makoto-Araki/powerful2025-item-register.git
```

### 開発準備
```bash
## Python仮想環境起動
$ python3 --version
$ python3 -m venv venv
$ source venv/bin/activate

## Pythonライブラリのインストール
$ pip install -r requirements.txt

## 設定ファイル作成
$ echo 'ACCESS_TOKEN=(APIトークン)' >> .env
$ echo '.env' >> .gitignore
$ echo 'venv/' >> .gitignore
$ echo 'input/' >> .gitignore

## Python仮想環境終了
$ deactivate
```

### 開発作業
```bash
## Python仮想環境起動
$ source venv/bin/activate

## 入力CSVファイル用のディレクトリ作成
$ mkdir input

## 入力CSVファイル作成
$ vi input_csv_01.csv

## Pythonプログラム記述
$ vi main.py

## Pythonプログラム実行
$ python3 main.py

## コミットとリモートリポジトリにプッシュ
$ git add .
$ git commit -m 新規作成
$ git push origin main

## Python仮想環境終了
$ deactivate
```
