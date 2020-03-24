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
import urllib.request
import lxml.html

client = discord.Client()

#riotwacherの設定
yaml_dict = yaml.load(open('secret.yaml').read(), Loader=yaml.SafeLoader)
lol_watcher = LolWatcher(yaml_dict['riotapi_key'])
my_region = 'jp1'

#embed用変数
auther_icon = 'https://raw.githubusercontent.com/AdiosSora/DiscordBot_SoramanNo.2/master/pics/lol_icon.png'
summoner_spell = {'SummonerBarrier':'<:SummonerBarrier:692104473564151869>','SummonerBoost':'<:SummonerBoost:692104473551568918>','SummonerDot':'<:SummonerDot:692104473820135455>','SummonerExhaust':'<:SummonerExhaust:692104473799032864>','SummonerFlash':'<:SummonerFlash:692104473375539211>','SummonerHaste':'<:SummonerHaste:692104473384058972>','SummonerHeal':'<:SummonerHeal:692104473358762015>','SummonerMana':'<:SummonerMana:692104473740443678>','SummonerSmite':'<:SummonerSmite:692104473732186142>','SummonerTeleport':'<:SummonerTeleport:692104473560219743>'}
#opggスクレイピング設定
def opgg_update():
    url = 'http://jp.op.gg/champion/statistics' #opggの統計ページを指定
    response = urllib.request.urlopen(url)
    opgg_data = lxml.html.fromstring(response.read())   #opggの統計ページをxpathで要素指定出来るように変換
    rolelist = ['TOP','JUNGLE','MID','ADC','SUPPORT']   #roleリスト
    tier_list = []  #role毎のリストを追加する用のリストを設定
    for role in rolelist:   #role分ループ
        tier_length = int(opgg_data.xpath("count(//tbody[@class='tabItem champion-trend-tier-"+ role +"']/tr)")) #role毎のチャンピオン数をカウント
        roletier_list = []  #roleのデータを追加する用のリストを設定
        for index in range(tier_length):    #roleのチャンピオン数だけループしデータをroletier_listに追加する。
            champion_name = opgg_data.xpath("string(//tbody[@class='tabItem champion-trend-tier-"+ role +"']/tr["+ str(index+1) +"]/td[4]/a/div[1])")
            champion_winrate = opgg_data.xpath("string(//tbody[@class='tabItem champion-trend-tier-"+ role +"']/tr["+ str(index+1) +"]/td[5])")
            champion_pickrate = opgg_data.xpath("string(//tbody[@class='tabItem champion-trend-tier-"+ role +"']/tr["+ str(index+1) +"]/td[6])")
            champion_url = opgg_data.xpath("//tbody[@class='tabItem champion-trend-tier-"+ role +"']/tr["+ str(index+1) +"]/td[4]/a/@href")
            roletier_list.append([champion_name,champion_winrate,champion_pickrate,'http://jp.op.gg'+champion_url[0]])
        tier_list.append(roletier_list)
    return tier_list

def riotjson_update():#jsonを最新にアップデート
    #チャンピオンの情報をjson形式で取得
    league_of_legends_version = requests.get('https://ddragon.leagueoflegends.com/api/versions.json')
    latest_version_json = league_of_legends_version.json()
    #lolの最新バージョンの値を取得
    champion_get_json = requests.get('http://ddragon.leagueoflegends.com/cdn/'+str(latest_version_json[0])+'/data/ja_JP/champion.json')
    champion_json = champion_get_json.json()
    return latest_version_json,champion_json


riot_api_version,riot_champion_json = riotjson_update()
tier_list = opgg_update()

# コグとして用いるクラスを定義。
class MainCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def lol(self,ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(title='サブコマンドが設定されていません。',description='free / tier / status', color=0x79ffff)    #embedのタイトルと色を設定
            embed.set_author(name="LoL Command", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
            await ctx.send(embed=embed) #embed出力

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

        #チャンピオンのアイコンURをリストに追加
        for champion_name in freechampion_name_list:
            freechampion_icon_list.append('http://ddragon.leagueoflegends.com/cdn/'+riot_api_version[0]+'/img/champion/'+champion_name+'.png')
        fcil_len_helf = math.ceil(len(freechampion_icon_list)/2)

        #アイコンURLからローカルに保存
        def icon_download(list,index):
            file_name = 'pics/champion_icon.png'
            response = requests.get(list[index])
            image = response.content
            with open(file_name, "wb") as aaa:
                aaa.write(image)
            return file_name
        img_1 = cv2.imread(icon_download(freechampion_icon_list,0)) #ローカルに保存した画像をcv2で読み込む
        img_2 = cv2.imread(icon_download(freechampion_icon_list,fcil_len_helf)) #ローカルに保存した画像をcv2で読み込む
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

        #フリーチャンピオン一覧を送信後ローカルファイルを削除
        await ctx.channel.send(file=discord.File('pics/freechampion_listimage.jpg'))
        os.remove('pics/champion_icon.png')
        os.remove('pics/freechampion_listimage.jpg')

    @lol.command()
    async def tier(self,ctx,lanename=None):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        lanelist = [['top'],['jg'],['mid'],['adc'],['sup']]
        lane_index = 99
        for index in range(len(lanelist)):
            if str(lanename) in lanelist[index]:
                lane_index = index
        if lane_index == 99:
            embed=discord.Embed(title='レーンが選択されてません',description='top/jg/mid/adc/supのいずれかを選択してください。', color=0x79ffff)    #embedのタイトルと色を設定
            embed.set_author(name="LoL Tier List", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
            await ctx.send(embed=embed) #embed出力
        else:
            page_count = 0 #ページカウントを初期化
            page_length = int(len(tier_list[lane_index])/5 if len(tier_list[lane_index])%5 == 0 else len(tier_list[lane_index])/5+1)   #合計のページ数を代入
            embed=discord.Embed(title='Top Tier(1~5)',description='OPGGのデータを元にチャンピオンTierを表示します。', color=0x79ffff)    #embedのタイトルと色を設定
            embed.set_author(name="LoL Tier List", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
            for index in range(5):  #上位5チャンピオンの名前、勝率、ピック率をembedに追加
                r_champion_name = tier_list[lane_index][index][0]
                r_win_rate = tier_list[lane_index][index][1]
                r_pick_rate = tier_list[lane_index][index][2]
                embed.add_field(name='チャンピオン名', value=str(index+1) +" "+ r_champion_name, inline=True)
                embed.add_field(name='勝率', value=r_win_rate, inline=True)
                embed.add_field(name='ピック率', value=r_pick_rate, inline=True)
            embed.set_footer(text="[1/"+str(page_length)+"]")   #フッターにページ数を表示
            msg = await ctx.send(embed=embed) #embed出力
            reaction_list = ["⬅","➡","1️⃣","2️⃣","3️⃣","4️⃣","5️⃣"] #必要なリアクションを設定
            for index in range(6):  #初期ページ用リアクションをメッセージにリアクションする
                await msg.add_reaction(reaction_list[index+1])  #初期リアクションをつける
            def check(react, user):
                #コマンド投稿者とリアクション者が同一、リアクションが設定されているもの、リアクションされたメッセージがBotが投稿したメッセージであるかをチェック
                return user == ctx.author and str(react) in reaction_list and react.message.id == msg.id

            while not client.is_closed(): #タイムアウトするまでリアクション受付を継続

                try:
                    user,react = await self.bot.wait_for('reaction_add', check=check, timeout=30.0) #リアクションを30秒待受する。

                except asyncio.TimeoutError:    #タイムアウトした場合
                    await msg.clear_reactions()
                    await msg.add_reaction('✖')
                    return
                else:   #リアクションの受付に成功した場合
                    emoji = str(user)
                    page_count_now = page_count
                    if emoji == "⬅" or emoji == "➡":
                        if emoji == "⬅":
                            page_count-=1   #ページ数を減らす
                            await msg.clear_reactions()#リアクションをリセット
                        elif emoji == "➡":
                            page_count+=1   ##ページ数を増やす
                            await msg.clear_reactions()#リアクションをリセット
                        embed=discord.Embed(title=lanelist[lane_index][0]+' Tier('+str(page_count*5+1)+'~'+str((page_count*5)+5)+')',description='OPGGのデータを元にチャンピオンTier順位を表示します。', color=0x79ffff)    #embedのタイトルと色を設定
                        embed.set_author(name="LoL Tier List", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
                        if page_count_now != page_count and page_count != page_length-1:
                            insert_field = 5
                        elif page_count_now != page_count and page_count == page_length-1:
                            insert_field = len(tier_list[0])%5
                        for index in range(insert_field):
                            r_champion_name = tier_list[lane_index][page_count*5+index][0]
                            r_win_rate = tier_list[lane_index][page_count*5+index][1]
                            r_pick_rate = tier_list[lane_index][page_count*5+index][2]
                            embed.add_field(name='チャンピオン名', value=str(index+1) +" "+ r_champion_name, inline=True)
                            embed.add_field(name='勝率', value=r_win_rate, inline=True)
                            embed.add_field(name='ピック率', value=r_pick_rate, inline=True)
                        embed.set_footer(text="["+str(page_count+1)+"/"+str(page_length)+"]")
                        await msg.edit(embed=embed)

                        if page_count == 0:
                            for index in range(6):
                                await msg.add_reaction(reaction_list[index+1])  #初期リアクションをつける
                        elif 0 < page_count < page_length-1:
                            for index in range(7):
                                await msg.add_reaction(reaction_list[index])  #初期リアクションをつける
                        elif page_count+1 == page_length:
                            for index in range(7):
                                if index != 1:
                                    await msg.add_reaction(reaction_list[index])  #初期リアクションをつける
                    else:
                        await msg.clear_reactions()
                        await msg.add_reaction('✖')
                        champion_index = reaction_list.index(emoji)-2
                        url = tier_list[0][page_count*5+champion_index][3] #opggのチャンピオンページを取得
                        response = urllib.request.urlopen(url)
                        opgg_data_champion = lxml.html.fromstring(response.read())   #opggの統計ページをxpathで要素指定出来るように変換
                        skillorder = [
                            opgg_data_champion.xpath("string(//ul[@class='champion-stats__list']/li[1]/span[1])"),
                            opgg_data_champion.xpath("string(//ul[@class='champion-stats__list']/li[3]/span[1])"),
                            opgg_data_champion.xpath("string(//ul[@class='champion-stats__list']/li[5]/span[1])")
                        ]
                        summonerspell = [opgg_data_champion.xpath("//ul[@class='champion-stats__list']/li[1]/img[1]/@src"),opgg_data_champion.xpath("//ul[@class='champion-stats__list']/li[3]/img[1]/@src")]
                        for index in range(len(summonerspell)):
                            summonerspell[index][0] = summonerspell[index][0].split('spell/')[-1].split('.png')[0]
                            print(str(summonerspell[index][0]))
                        skillbuild = ''
                        for index in range(12):
                            skillbuild += opgg_data_champion.xpath("string(//table[@class='champion-skill-build__table']/tbody/tr[2]/td["+str(index+1)+"])")
                            if index != 11:
                                skillbuild += ' > '
                        skillbuild = skillbuild.replace('	','')
                        skillbuild = skillbuild.replace('\n','')
                        champion_id = ''
                        for champion in riot_champion_json['data']:    #チャンピオンの数だけループ
                            if riot_champion_json['data'][champion]['name'] == tier_list[lane_index][page_count*5+champion_index][0]:
                                champion_id = riot_champion_json['data'][champion]['id']
                        champion_get_json = requests.get('http://ddragon.leagueoflegends.com/cdn/'+str(riot_api_version[0])+'/data/ja_JP/champion/'+champion_id+'.json')
                        champion_json = champion_get_json.json()
                        embed=discord.Embed(title=tier_list[lane_index][page_count*5+champion_index][0],description=tier_list[0][page_count*5+champion_index][0]+'の詳細情報を表示します。', color=0x79ffff)    #embedのタイトルと色を設定
                        embed.set_author(name="LoL ChampionDetail", icon_url=auther_icon)   #embedのアイコンと投稿者名を設定
                        embed.set_thumbnail(url="http://ddragon.leagueoflegends.com/cdn/"+str(riot_api_version[0])+"/img/champion/"+champion_id+".png")     #サモナーアイコンを設定
                        embed.add_field(name='勝率', value=tier_list[lane_index][page_count*5+champion_index][1], inline=True)
                        embed.add_field(name='ピック率', value=tier_list[lane_index][page_count*5+champion_index][2], inline=True)
                        embed.add_field(name='スキル優先度',value=skillorder[0]+'>'+skillorder[1]+'>'+skillorder[2], inline=False)    #embedのタイトルと色を設定
                        embed.add_field(name='スキルオーダー', value=skillbuild, inline=False)
                        embed.add_field(name='サモナースペル', value=summoner_spell[summonerspell[0][0]]+summoner_spell[summonerspell[1][0]], inline=False)
                        await ctx.send(embed=embed) #embed出力

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
