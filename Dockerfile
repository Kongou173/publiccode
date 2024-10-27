# Pythonイメージを使用
FROM python:3.11-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なファイルをコンテナにコピー
COPY requirements.txt .
COPY main.py .
COPY keep_alive.py .

# 依存関係をインストール
RUN pip install --no-cache-dir -r requirements.txt

# Botを起動する
CMD ["python", "main.py"]

