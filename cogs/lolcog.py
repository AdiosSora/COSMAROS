import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio
import math
from decimal import *
import yaml
from riotwatcher import LolWatcher, ApiError

client = discord.Client()
yaml_dict = yaml.load(open('secret.yaml').read(), Loader=yaml.SafeLoader)
lol_watcher = LolWatcher(yaml_dict['riotapi_key'])
my_region = 'jp1'
# コグとして用いるクラスを定義。
class MainCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def lol(self,ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    @lol.command()
    async def status(self,ctx,summoner_name=None):
        summoner = lol_watcher.summoner.by_name(my_region, summoner_name)
        league = lol_watcher.league.by_summoner(my_region, summoner['id'])
        embed=discord.Embed(title=summoner_name,url='https://jp.op.gg/summoner/userName='+str(summoner_name) ,description='Lv.' + str(summoner['summonerLevel']), color=0x79ffff)
        embed.set_author(name="LoL Status", icon_url='https://raw.githubusercontent.com/AdiosSora/DiscordBot_SoramanNo.2/master/pics/lol_icon.png')
        embed.set_thumbnail(url="https://opgg-static.akamaized.net/images/profile_icons/profileIcon"+str(summoner['profileIconId'])+".jpg")
        if len(league)!=0:
            win = int(league[0]['wins'])
            losses = int(league[0]['losses'])
            winrate = '{:.0%}'.format(Decimal(str(win/(win+losses))).quantize(Decimal('.01'), rounding=ROUND_UP))
            embed.add_field(name="Tier", value=str(league[0]['tier'])+' '+str(league[0]['rank']), inline=True)
            embed.add_field(name="Winrate", value=str(winrate), inline=True)
        else:
            embed.add_field(name="Tier", value='ランクデータがありません。', inline=False)
        embed.set_footer(text="#lol status " + summoner_name)
        await ctx.send(embed=embed)

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
