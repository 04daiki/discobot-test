import discord

intents = discord.Intents.default()
intents.messages = True

client = discord.Client(intents=intents)

# Discordトークン（あなたのトークンに置き換えてください）
TOKEN = ''

# クライアントの初期化
# client = discord.Client()

# メッセージが送信されたときのイベント
@client.event
async def on_message(message):
    # Bot自身のメッセージには反応しない
    if message.author == client.user:
        return
    
    # ユーザーからのメッセージに「こんにちは」と返答する
    if message.content:
        await message.channel.send('こんにちは！')

# Botの実行
client.run(TOKEN)