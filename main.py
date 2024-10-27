import discord
from discord.ext import commands
import pytz
from datetime import datetime
from keep_alive import keep_alive  # keep_alive.pyから関数をインポート

# Discordのトークンをここに入力
TOKEN = 'YOUR_DISCORD_BOT_TOKEN'  # トークンを忘れずに置き換える

# Intentsの設定（必要なものを有効化）
intents = discord.Intents.default()

# Botの初期化（CommandTreeは自動で紐づけされる）
client = commands.Bot(command_prefix='!', intents=intents)

# 東京の現在時刻を取得する関数
def get_tokyo_time():
    tz = pytz.timezone('Asia/Tokyo')
    now = datetime.now(tz)
    return now.strftime('%Y-%m-%d %H:%M:%S')

# /time コマンドを登録
@client.tree.command(name="time", description="現在の東京の時刻を表示します")
async def time(interaction: discord.Interaction):
    tokyo_time = get_tokyo_time()
    await interaction.response.send_message(f"現在の東京の時刻: {tokyo_time}")

# /support コマンドを登録
@client.tree.command(name="support", description="サポート用のDiscordサーバーリンクを表示します")
async def support(interaction: discord.Interaction):
    support_link = "https://discord.gg/your_server_link"  # 適切なリンクに変更
    await interaction.response.send_message(f"こちらがサポート用のサーバーリンクです: {support_link}")

# Botの準備が整ったときに呼び出されるイベント
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

    try:
        synced = await client.tree.sync()
        print(f"{len(synced)} 個のコマンドが同期されました。")
    except discord.HTTPException as e:
        print(f"コマンドの同期に失敗しました: {e}")

# Botを維持するためのサーバーを起動し、Botを実行
if __name__ == "__main__":
    keep_alive()  # サーバーを維持
    client.run(TOKEN)  # Botを起動
