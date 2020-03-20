import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio

client = discord.Client()

# コグとして用いるクラスを定義。
class MainCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send('pong!')

    @commands.command()
    async def mention(self, ctx):
        reply = f'{ctx.author.mention} 呼んだ？' # 返信メッセージの作成
        await ctx.channel.send(reply)

    @commands.command()
    async def help(self, ctx):
        page_count = 0 #ページカウントを初期化
        embed=discord.Embed(title="ヘルプページ", description="基本コマンド", color=0xffff00) #現在のヘルプページのembedを挿入
        embed.add_field(name='help', value='コマンドのヘルプを確認できます。リアクションを押すことでページ遷移できます。', inline=False)
        embed.add_field(name='ping', value='pongを返します。', inline=False)
        embed.add_field(name='mention', value='メンションを送信者に送ります。', inline=False)
        embed.set_footer(text="[1/6]")
        msg = await ctx.send(embed=embed) #embed出力
        await msg.add_reaction("➡") #初期リアクションをつける

        def check(react, user):
            return user == ctx.author and (str(react) == "⬅" or str(react) == "➡") and react.message.id == msg.id

        while not client.is_closed(): #タイムアウトするまでリアクション受付を継続

            try:
                user,react = await self.bot.wait_for('reaction_add', check=check, timeout=30.0)

            except asyncio.TimeoutError:
                await msg.clear_reactions()
                await msg.add_reaction('✖')
                return

            else:
                emoji = str(user)

                if emoji == "⬅":
                    page_count-=1
                elif emoji == "➡":
                    page_count+=1

                await msg.clear_reactions()#リアクションをリセット
                if page_count == 0:
                    embed=discord.Embed(title="ヘルプページ", description="基本コマンド", color=0xffff00) #現在のヘルプページのembedを挿入
                    embed.add_field(name='help', value='コマンドのヘルプを確認できます。リアクションを押すことでページ遷移できます。', inline=False)
                    embed.add_field(name='ping', value='pongを返します。', inline=False)
                    embed.add_field(name='mention', value='メンションを送信者に送ります。', inline=False)
                elif page_count == 1:
                        embed=discord.Embed(title="ヘルプページ",description="チーム分け機能", color=0xffff00) #現在のヘルプページのembedを挿入
                        embed.add_field(name='前提要求', value='ボイスチャンネル「custom_general」テキストチャンネル「custom-1」「custom-2」役職「Custom-1」「Custom-2」を用意してください。', inline=False)
                        embed.add_field(name='custom start', value='「custom_general」チャンネルに入室している10名を自動的に2チームに振り分けると同時に役職を付与します。10名以上の場合はランダムに10名選出されます。10名以下では利用できません。', inline=False)
                        embed.add_field(name='custom suffle', value='振り分けられたチームを完全にシャッフルして再度2チームに振り分けます。', inline=False)
                        embed.add_field(name='custom list', value='チーム関係なく10名全員のリストを表示します。', inline=False)
                        embed.add_field(name='custom teamlist', value='チーム毎のメンバーリストを表示します。', inline=False)
                        embed.add_field(name='custom change [数字] [数字]', value='チームメンバーリスト等で表示された番号を指定することでチーム間のメンバー移動が出来ます。', inline=False)
                        embed.add_field(name='custom win [red or blue]', value='勝利したチームを指定することでチームメンバー全員に勝利数が1追加されます。', inline=False)
                        embed.add_field(name='custom result', value='チーム振り分け機能が終了するまでに最多の勝利数を獲得したメンバーを表示します。', inline=False)
                        embed.add_field(name='custom end', value='振り分け機能を終了します。メンバーに付けた役職の自動解除、専用テキストチャンネルのログリセット、戦績のリセットを行います。', inline=False)
                elif page_count == 2:
                        embed=discord.Embed(title="ヘルプページ",description="League of Legends", color=0xffff00) #現在のヘルプページのembedを挿入
                        embed.add_field(name='lol status [サモナーネーム]', value='サモナーの情報を表示します。', inline=False)
                        embed.add_field(name='lol free', value='今週のフリーチャンピオンを表示します。', inline=False)
                embed.set_footer(text="["+str(page_count+1)+"/3]")
                await msg.edit(embed=embed)

                if page_count == 0:
                    await msg.add_reaction("➡")
                elif 0 < page_count < 2:
                    await msg.add_reaction("⬅")
                    await msg.add_reaction("➡")
                elif page_count == 2:
                    await msg.add_reaction("⬅")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == "そらまん":
            await message.channel.send('呼んだ？')

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.remove_command('help')
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
