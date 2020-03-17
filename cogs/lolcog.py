import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio
import math
from decimal import *
import yaml
from riotwatcher import LolWatcher, ApiError
import json
import requests
import cv2
import os

client = discord.Client()

#riotwacherの設定
yaml_dict = yaml.load(open('secret.yaml').read(), Loader=yaml.SafeLoader)
lol_watcher = LolWatcher(yaml_dict['riotapi_key'])
my_region = 'jp1'

#embed用変数
auther_icon = 'https://raw.githubusercontent.com/AdiosSora/DiscordBot_SoramanNo.2/master/pics/lol_icon.png'

def riotjson_update():#jsonを最新にアップデート
    #チャンピオンの情報をjson形式で取得
    league_of_legends_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    latest_version_json = league_of_legends_version.json()
    #lolの最新バージョンの値を取得
    champion_get_json = requests.get('http://ddragon.leagueoflegends.com/cdn/'+str(latest_version_json[0])+'/data/ja_JP/champion.json')
    champion_json = champion_get_json.json()
    return latest_version_json,champion_json

riot_api_version,riot_champion_json = riotjson_update()

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
        try:
            summoner = lol_watcher.summoner.by_name(my_region, summoner_name)   #riotwatcherでサモナーネームから情報を取得
            league = lol_watcher.league.by_summoner(my_region, summoner['id'])  #riotwatcher取得したサモナーIDのリーグ情報を取得
            embed=discord.Embed(title=summoner_name,url='https://jp.op.gg/summoner/userName='+str(summoner_name) ,description='Lv.' + str(summoner['summonerLevel']), color=0x79ffff)   #embedのタイトルとサモナーレベル表示を設定
            embed.set_author(name="LoL Status", icon_url=auther_icon)   #embedの投稿者とアイコンを設定
            embed.set_thumbnail(url="http://ddragon.leagueoflegends.com/cdn/10.5.1/img/profileicon/"+str(summoner['profileIconId'])+".png")     #サモナーアイコンを設定
            if len(league)!=0:  #今シーズンのランクデータが存在するか
                win = int(league[0]['wins'])    #今シーズのランクの勝利数を取得
                losses = int(league[0]['losses'])   #今シーズのランクの敗北数を取得
                winrate = '{:.0%}'.format(Decimal(str(win/(win+losses))).quantize(Decimal('.01'), rounding=ROUND_UP))   #今シーズンのランクの勝率を算出
                embed.add_field(name="Tier", value=str(league[0]['tier'])+' '+str(league[0]['rank']), inline=True)  #今シーズンのティアーをembedに追加
                embed.add_field(name="Winrate", value=str(winrate), inline=True)    #今シーズンの勝率をembedに追加
            else:   #ランクデータが存在しなかった場合
                embed.add_field(name="Tier", value='ランクデータなし', inline=False)
        except ApiError as err:
            if err.response.status_code == 404:     #サモナー名が存在しないなどのエラーが返ってきた場合
                embed=discord.Embed(title="サモナーが見つかりません。" ,description="", color=0xc93f3f)  #エラー用embedのタイトルを設定
                embed.set_author(name="LoL Status", icon_url=auther_icon)   #embedの投稿者とアイコンを設定
            else:
                raise
        embed.set_footer(text="#lol status " + summoner_name)   #embedのフッターにコマンドを設定
        await ctx.send(embed=embed)     #embedを送信

    @lol.command()
    async def free(self,ctx):
        freechampion = lol_watcher.champion.rotations(my_region)    #riotwatcherでフリーチャンピオンの一覧を取得
        freeChampionIds = freechampion['freeChampionIds']   #フリーチャンピオンのIDのみを取得
        embed=discord.Embed(title='今週のフリーチャンピオン',description='', color=0x79ffff)    #embedのタイトルと色を設定
        embed.set_author(name="LoL Status", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
        freechampion_count = 0  #フリーチャンピオンをカウントする変数を初期化
        freechampion_name_list = [] #フリーチャンピオン名のリスト変数を初期化

        #フリーチャンピオンを取得してembedに追加する
        for champion_name in riot_champion_json['data']:    #チャンピオンの数だけループ
            if int(riot_champion_json['data'][champion_name]['key']) in freeChampionIds:    #チャンピオンのIDとフリーチャンピオンのIDが一致した時
                freechampion_count += 1
                champion_name_ja = riot_champion_json['data'][champion_name]['name']    #日本語チャンピオン名を取得
                freechampion_name_list.append(champion_name)
                embed.add_field(name=champion_name,value=champion_name_ja, inline=True) #embedのフィールドにフリーチャンピオンを追加

        #フリーチャンピオンのアイコン一覧を作成
        freechampion_icon_list = []
        for champion_name in freechampion_name_list:
            freechampion_icon_list.append('http://ddragon.leagueoflegends.com/cdn/'+riot_api_version[0]+'/img/champion/'+champion_name+'.png')
        fcil_len_helf = math.ceil(len(freechampion_icon_list)/2)
        img_1 = cv2.imread(icon_download(freechampion_icon_list,0))
        img_2 = cv2.imread(icon_download(freechampion_icon_list,fcil_len_helf))
        for index in range(fcil_len_helf):
            if index != 0 and fcil_len_helf > index :
                img_1_1 = cv2.imread(icon_download(freechampion_icon_list,index))
                img_1 =cv2.hconcat([img_1, img_1_1])
                if index+fcil_len_helf < len(freechampion_icon_list):
                    img_2_2 = cv2.imread(icon_download(freechampion_icon_list,fcil_len_helf+index))
                    img_2 =cv2.hconcat([img_2, img_2_2])
        img_lol_icon = cv2.imread('pics/bot_icon_bg.png')
        img_2 =cv2.hconcat([img_2, img_lol_icon])
        img_3 = cv2.vconcat([img_1, img_2])
        cv2.imwrite('pics/freechampion_listimage.jpg', img_3)
        embed.set_footer(text="#lol free")  #embedのフッターにコマンドを表示
        await ctx.send(embed=embed) #embedを送信
        await ctx.channel.send(file=discord.File('pics/freechampion_listimage.jpg'))
        os.remove('pics/champion_icon.png')
        os.remove('pics/freechampion_listimage.jpg')

def icon_download(list,index):
    file_name = 'pics/champion_icon.png'
    response = requests.get(list[index])
    image = response.content
    with open(file_name, "wb") as aaa:
        aaa.write(image)
    return file_name
# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
