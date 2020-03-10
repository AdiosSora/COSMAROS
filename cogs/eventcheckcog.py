import discord
from discord.ext import commands # Bot Commands Frameworkのインポート
import asyncio
import datetime
import calendar
from config import googlecalender

client = discord.Client()

# コグとして用いるクラスを定義。
class MainCog(commands.Cog):
    # TestCogクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ein(self, ctx, e_title=None, e_description=None, e_month=None, e_day=None): #予定入力コマンド
        gc_icon = "https://image.flaticon.com/icons/png/512/720/premium/720329.png" #GooglecalendarのアイコンURL
        error_description = "" #エラーを確認した時に通知に表示する内容を格納する文字列変数。
        error_flag = False #エラーを確認するためのフラグ変数。
        dt_now = datetime.datetime.now() #コマンド入力時の日付を取得。
        g_connect = googlecalender.googlecalender_connect

        #入力コマンドのエラーチェック

        if e_title!=None: #予定の題名が入力されているか

            if e_description!=None : #予定の内容が入力されているか

                if e_month!=None : #月が入力されているか

                    if e_day!=None : #日が入力されているか
                        error_flag = True

                    else:
                        error_description = "日付(日)" #日付の日が入力されていない場合

                else:#月の内容が入力されていない場合
                    error_description = "日付" #日付の月が入力されていない場合

            else: #予定の内容が入力されていない場合
                error_description = "予定内容" #予定内容が入力されていない場合

        else: #予定の題名が入力されていない場合
            error_description = "予定" #予定の題名が入力されていない場合

        #Discord側への通知処理。

        if e_month != None and e_day != None:
            try: #日付をStringからintにキャストしたときのエラーチェック
                e_month = int(e_month)#String to intへキャスト
                e_day = int(e_day)#String to intへキャスト
                e_yearlater_month = 12 if e_month == 1 else e_month-1 #1年後の月を指定
                e_year = dt_now.year+1 if e_month < dt_now.month else dt_now.year #月に応じた年度指定

            except ValueError: #日付に数値が使われなかった場合
                error_description = "日付は数字を"
                error_flag = False


        if error_flag == True: #エラーが一度も出なかった場合正常と判断して、予定追加処理を実行と表示を行う。

            if 1 <= e_month <= 12 and 1 <= e_day <= calendar.monthrange(dt_now.year, e_month)[1]:#日付がカレンダーの入力できる値に収まっているか。
                embed=discord.Embed(title="", color=0x00ff00)
                embed.set_author(name="予定を追加しました。", url=gc_icon,
                icon_url=gc_icon)
                embed.add_field(name="予定", value=e_title, inline=True)
                embed.add_field(name="日付", value=str(e_year) + "/" + str(e_month) + "/" + str(e_day), inline=True)
                embed.add_field(name="内容", value=e_description, inline=False)

            else: #エラーを確認したため取得したエラーの内容を表示する。
                embed=discord.Embed(title="", color=0xff0000)
                embed.set_author(name="エラー", url=gc_icon,
                icon_url=gc_icon)
                embed.add_field(name="エラー内容", value="正しい日付を入力してください。", inline=True)

            g_connect.insert_event(e_title,e_description,e_year,e_month,e_day)
        else:#日付がカレンダーの入力できる値に収まっていない場合。
            embed=discord.Embed(title="", color=0xff0000)
            embed.set_author(name="エラー", url=gc_icon,
            icon_url=gc_icon)
            embed.add_field(name="エラー内容", value=error_description + "を入力してください。", inline=True)

        await ctx.send(embed=embed) #embed出力



# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(MainCog(bot)) # TestCogにBotを渡してインスタンス化し、Botにコグとして登録する。
