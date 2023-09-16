
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def main():
    # ここに画像処理と分岐をする
    # 状態判定Flask

    # status == 2 -> busy
    # status == 1 -> soso
    # status == 0 -> empty
    filePath = "index.html"
    with open(filePath, encoding='UTF-8') as f:
        return f.read()
