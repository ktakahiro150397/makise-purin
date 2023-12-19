import asyncio
import json
from logging import config, getLogger
import sys
import textwrap
import traceback
from typing import Sequence
from discord import FFmpegPCMAudio, app_commands
import logging.handlers
import discord
import os
from dotenv import main
from datetime import datetime


# 環境変数を読み込み
main.load_dotenv()

# ログ設定読込
with open("logSettings.json") as f:
    config.dictConfig(json.load(f))
logger = getLogger(__name__)

# Discordクライアントのインスタンス化
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents,proxy=os.getenv("PROXY"))
tree = app_commands.CommandTree(client)

# discord側で反応するチャンネルのIDリスト。
responseChannelArray = os.getenv("DISCORD_RESPONSE_CHANNEL_ID").split(",")
responseChannel = [int(val) for val in responseChannelArray]
logger.info(f"反応対象のチャンネルIDは次の通りです。{responseChannel}")


@client.event
async def on_ready():
    logger.debug(f"Called : {sys._getframe().f_code.co_name}")
    await tree.sync()
    logger.info(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    logger.debug(f"Called : {sys._getframe().f_code.co_name}")
    logger.debug(message)

    if message.channel.id not in responseChannel:
        logger.info(f"反応対象のチャンネルIDではありません。チャンネルID：{message.channel.id}")  
        return

    if message.author == client.user:
        logger.info("送信者が本人のため、何もしない")
        return
    
    if message.content.startswith("#"):
        logger.info("先頭が#のため、何もしない")
        return
    
    # ここで応答処理
    async with message.channel.typing():
        try:
            await message.channel.send("message received.")
        except Exception as e:
            error_message = traceback.format_exc()
        
            logger.error(f"エラーが発生しました。\n{error_message}")
            await message.channel.send(f"エラーが発生しました。\n\n{error_message[-1800:]}")


@tree.command(name="play",description="牧瀬紅莉栖が歌ってくれます。")
async def play(interaction:discord.Interaction):
    await interaction.response.defer()

    # ボイスチャンネルに接続
    if interaction.user.voice is None:
        await interaction.followup.send("まずボイスチャンネルに接続してください！")
        return
    
    bot_connected_channel = list(filter(lambda x: x.channel.id == interaction.user.voice.channel.id, interaction.client.voice_clients))
    if len(bot_connected_channel) > 0:
        # 既に接続している場合は、何もしない
        await interaction.followup.send("既に接続しています。")
    else:
        bot_connected_channel = await interaction.user.voice.channel.connect()
        await interaction.followup.send("接続しました。")

        # 音声ファイルを再生
        bot_connected_channel.play(FFmpegPCMAudio("content/LOST GARDEN.mp3"))

# クライアントを実行
discord.utils.setup_logging()
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
client.run(DISCORD_BOT_TOKEN)