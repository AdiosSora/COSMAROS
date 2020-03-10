import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio

client = discord.Client()

# コグとして用いるクラスを定義。
class MainCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
