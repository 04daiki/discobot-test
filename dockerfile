# Pythonの軽量版をベースに使用
FROM python:3.9-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要な依存関係をインストール
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ソースコードをコンテナ内にコピー
COPY . .

# Botを実行
CMD ["python", "bot.py"]