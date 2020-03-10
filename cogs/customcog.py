import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio
import random
import math

client = discord.Client()

member_list = []
team_on_flag = False
emoji_number_list = [':one: ',':two: ',':three: ',':four: ',':five: ',':six: ',':seven: ',':eight: ',':nine: ',':keycap_ten: ']

# コグとして用いるクラスを定義。
class CustomCog(commands.Cog):
    # CustomCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def custom(self,ctx):
        # サブコマンドが指定されていない場合、メッセージを送信する。
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。')

    @custom.command()
    async def start(self,ctx):
        #グローバル変数を再代入するための宣言
        global team_on_flag,member_list
        #カスタムが始まった為、フラグをTrueに
        team_on_flag = True
        await ctx.channel.send('カスタム(通常モード)を開始します。')

        # 集計するボイスチャンネルと出力するテキストチャンネルを設定
        channel = discord.utils.get(ctx.guild.voice_channels, name='custom_general')
        #メンバーを集計する前に配列をリセット
        member_list.clear()
        #メンバーを10人まで取得して配列に格納、取得したメンバーを表示
        member_count = 0
        embed = discord.Embed(title="メンバーリスト", color=0x00ffff)
        for member in channel.members:
            member_count+=1
            member_list.append([member,0])
            embed.add_field(name=member.display_name, value="player" + str(member_count), inline=True)
            if member_count>=10:
                break
        await ctx.channel.send(embed=embed)

        #カスタムのメンバーが10人になっているか比較
        if len(member_list) < 10:
            await ctx.channel.send('メンバーが10人未満の為、開始できません。')
        elif len(member_list) == 10:
            #カスタム参加者をシャッフルします
            embed = discord.Embed(title=":arrows_counterclockwise: シャッフル中...", color=0x00ffff)
            await ctx.channel.send(embed=embed)
            random.shuffle(member_list)

            #カスタム部屋用の役職２つを変数に格納
            role = discord.utils.get(ctx.guild.roles, name='Custom-1')
            role2 = discord.utils.get(ctx.guild.roles, name='Custom-2')

            #青チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/BLUE-TEAM-TRISTA.png'))
            embed = discord.Embed(title='　', color=0x0000ff)
            for var in range(0,5):
                #青チーム用ではない役職を削除して青チーム用の役職を付与
                await member_list[var][0].remove_roles(role2)
                await member_list[var][0].add_roles(role)
                embed.add_field(name=str(member_list[var][0].display_name), value=emoji_number_list[var]+f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)

            #赤チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/RED-TEAM-TEEMO.png'))
            embed = discord.Embed(title='　', color=0xff0000)
            for var in range(5,10):
                #赤チーム用ではない役職を削除して赤チーム用の役職を付与
                await member_list[var][0].remove_roles(role)
                await member_list[var][0].add_roles(role2)
                embed.add_field(name=str(member_list[var][0].display_name), value=emoji_number_list[var]+f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)

            embed = discord.Embed(title=':white_check_mark: チーム分けが完了しました', color=0x00ffff)
            await ctx.channel.send(embed=embed)

    @custom.command()
    async def shuffle(self,ctx):
        global team_on_flag,member_list
        if team_on_flag == True:
            embed = discord.Embed(title=":arrows_counterclockwise: シャッフル中...", color=0x00ffff)
            await ctx.channel.send(embed=embed)
            random.shuffle(member_list)

            #カスタム部屋用の役職２つを変数に格納
            role = discord.utils.get(ctx.guild.roles, name='Custom-1')
            role2 = discord.utils.get(ctx.guild.roles, name='Custom-2')

            #青チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/BLUE-TEAM-TRISTA.png'))
            embed = discord.Embed(title='　', color=0x0000ff)
            for var in range(0,5):
                #青チーム用ではない役職を削除して青チーム用の役職を付与
                await member_list[var][0].remove_roles(role2)
                await member_list[var][0].add_roles(role)
                embed.add_field(name=str(member_list[var][0].display_name), value=emoji_number_list[var]+f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)

            #赤チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/RED-TEAM-TEEMO.png'))
            embed = discord.Embed(title='　', color=0xff0000)
            for var in range(5,10):
                #赤チーム用ではない役職を削除して赤チーム用の役職を付与
                await member_list[var][0].remove_roles(role)
                await member_list[var][0].add_roles(role2)
                embed.add_field(name=str(member_list[var][0].display_name), value=emoji_number_list[var]+f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)
            embed = discord.Embed(title=':white_check_mark: シャッフルが完了しました', color=0x00ffff)
            await ctx.channel.send(embed=embed)
        else:
            #カスタムが開始されていなかった場合のエラーembedを送信
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def list(self,ctx):
        global team_on_flag,member_list
        if team_on_flag == True:
            #参加してるメンバーの一覧を表示します
            embed = discord.Embed(title="メンバーリスト", color=0x00ffff)
            for var in range(0,10):
                embed.add_field(name=member_list[var][0].display_name, value="player" + str(var+1), inline=True)
            await ctx.channel.send(embed=embed)
        else:
            #カスタムが開始されていなかった場合のエラーembedを送信
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def teamlist(self,ctx):
        global team_on_flag,member_list
        if team_on_flag == True:
            #青チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/BLUE-TEAM-TRISTA.png'))
            embed = discord.Embed(title='　', color=0x0000ff)
            for var in range(0,5):
                embed.add_field(name=emoji_number_list[var]+str(member_list[var][0].display_name), value=f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)

            #赤チームのメンバー表示
            await ctx.channel.send(file=discord.File('pics/RED-TEAM-TEEMO.png'))
            embed = discord.Embed(title='　', color=0xff0000)
            for var in range(5,10):
                embed.add_field(name=emoji_number_list[var]+str(member_list[var][0].display_name), value=f'{member_list[var][0].mention}', inline=True)
            embed.add_field(name='...', value='...', inline=True)
            await ctx.channel.send(embed=embed)
        else:
            #カスタムが開始されていなかった場合のエラーembedを送信
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def change(self,ctx,a: int,b: int):
        global team_on_flag
        global member_list
        if team_on_flag == True:
            if a == b:
                embed = discord.Embed(title=":warning: エラー", description="同一の指定は出来ません", color=0xff0000)
                await ctx.channel.send(embed=embed)
            elif a>=1 & a<=10 & b>=1 & b<=10:
                embed = discord.Embed(title=":arrows_counterclockwise: 入れ替えました。", description=member_list[a-1][0].display_name+"と"+member_list[b-1][0].display_name+"を入れ替えました", color=0x00ffff)
                await ctx.channel.send(embed=embed)

                #カスタム部屋用の役職２つを変数に格納
                role = discord.utils.get(ctx.guild.roles, name='Custom-1')
                role2 = discord.utils.get(ctx.guild.roles, name='Custom-2')

                if a <= 5:
                    await member_list[b-1][0].remove_roles(role2)
                    await member_list[b-1][0].add_roles(role)
                else:
                    await member_list[b-1][0].remove_roles(role)
                    await member_list[b-1][0].add_roles(role2)

                if b <= 5:
                    await member_list[a-1][0].remove_roles(role2)
                    await member_list[a-1][0].add_roles(role)
                else:
                    await member_list[a-1][0].remove_roles(role)
                    await member_list[a-1][0].add_roles(role2)

                temp = member_list[b-1]
                member_list[b-1] = member_list[a-1]
                member_list[a-1] = temp
            else:
                embed = discord.Embed(title=":warning: エラー", description="1から10の数値を指定してください", color=0xff0000)
                await ctx.channel.send(embed=embed)

        else:
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def end(self,ctx):
        global team_on_flag
        global member_list
        if team_on_flag == True:
            team_on_flag = False
            embed = discord.Embed(title=':arrow_forward: カスタムを終了します', color=0x00ffff)
            await ctx.channel.send(embed=embed)

            #テキストチャンネルのログをリセット

            #テキストチャンネルを格納
            channel_1 = discord.utils.get(ctx.guild.text_channels, name='custom-1')
            channel_2 = discord.utils.get(ctx.guild.text_channels, name='custom-2')

            #テキストチャンネルのログを初期化
            await channel_1.purge()
            await channel_2.purge()

            embed = discord.Embed(title='　', color=0x00ffff)
            embed.add_field(name=':wastebasket: テキストログ削除', value='custom-1を初期化しました', inline=False)
            embed.add_field(name=':wastebasket: テキストログ削除', value='custom-2を初期化しました', inline=False)

            #カスタム部屋用の役職２つを変数に格納
            role = discord.utils.get(ctx.guild.roles, name='Custom-1')
            role2 = discord.utils.get(ctx.guild.roles, name='Custom-2')

            #Custom-1役職を解除
            for var in range(0,5):
                await member_list[var][0].remove_roles(role)
            #Custom-2役職を解除
            for var in range(5,10):
                await member_list[var][0].remove_roles(role2)

            embed.add_field(name=':white_check_mark: 役職解除', value='参加しているメンバーの役職を解除しました', inline=False)
            await ctx.channel.send(embed=embed)


            embed = discord.Embed(title=':white_check_mark: カスタムが終了しました', color=0x00ffff)
            await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def win(self,ctx,team: str):
        global member_list,team_on_flag
        if team_on_flag == True:
            if team == 'blue':
                for var in range(0,5):
                    member_list[var][1] += 1
                embed = discord.Embed(title=":trophy: Blueチームの勝利", description="Blueチームのメンバーに勝利数を加えました", color=0x00ffff)
                await ctx.channel.send(embed=embed)
            elif team == 'red':
                for var in range(5,10):
                        member_list[var][1] += 1
                embed = discord.Embed(title=":trophy: Redチームの勝利", description="Redチームのメンバーに勝利数を加えました", color=0x00ffff)
                await ctx.channel.send(embed=embed)
            else:
                embed = discord.Embed(title=":warning: エラー", description="blueまたはredを指定してください。", color=0xff0000)
                await ctx.channel.send(embed=embed)
        else:
            await ctx.channel.send(embed=not_started())

    @custom.command()
    async def result(self,ctx,mode=None):
        global member_list,team_on_flag
        if mode is None:
            win_list = []
            for var in range(0,10):
                win_list.append(member_list[var][1])
            win_top = max(win_list)
            win_list = []
            for var in range(0,10):
                if win_top == member_list[var][1]:
                    win_list.append(var)
            await ctx.channel.send(file=discord.File('pics/Winner_poro.png'))
            embed = discord.Embed(title="　", color=0x00ffff)
            for var in range(len(win_list)):
                number = win_list[var]
                embed.add_field(name=':military_medal: ' + member_list[number][0].display_name, value="勝利数 : " + str(member_list[number][1]), inline=True)
            await ctx.channel.send(embed=embed)

        if mode == 'list':
            win_list = []
            embed = discord.Embed(title="<:riotfist:262997195685363713> メンバーリスト", color=0x00ffff)
            for var in range(0,10):
                win_list.append(member_list[var][1])
                embed.add_field(name=member_list[var][0].display_name, value="勝利数 : " + str(member_list[var][1]), inline=True)
            await ctx.channel.send(embed=embed)


def not_started():
    #エラーembed送信用
    embed = discord.Embed(title=":warning: エラー", description="カスタムは始まっていません", color=0xff0000)
    return embed

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(CustomCog(bot)) # CustomCogにBotを渡してインスタンス化し、Botにコグとして登録する。
