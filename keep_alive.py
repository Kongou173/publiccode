from flask import Flask
from threading import Thread

# Flaskアプリの初期化
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"  # Webサーバーで表示するメッセージ

# サーバーを実行する関数
def run():
    app.run(host='0.0.0.0', port=8080)

# スレッドでサーバーを維持する関数
def keep_alive():
    t = Thread(target=run)
    t.start()
