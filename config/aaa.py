if a is None or a == '1':
        embed = discord.Embed(title=':beginner: ヘルプページ',description="ページ[1]", color=0x00ffff)
        embed.add_field(name='help [番号]', value='ヘルプを表示します', inline=False)
        embed.add_field(name='role add', value='名誉そらまんランド国民役職を付与します。', inline=False)
        embed.set_footer(text="カスタム関係のコマンドは次のページへ")
        await ctx.channel.send(embed=embed)
    elif a == '2':
        embed = discord.Embed(title=':beginner: ヘルプページ',description="ページ[2]", color=0x00ffff)
        embed.add_field(name='custom start', value='custom_generalのメンバーを取得したのち、\nメンバーリストとチームリストを表示します。', inline=False)
        embed.add_field(name='custom shuffle', value='取得したメンバーからチームを再シャッフルして表示を行います。', inline=False)
        embed.add_field(name='custom change [番号1]　[番号2]', value='チームリストで表示される番号を指定して、\n番号1と番号2のメンバーを入れ替えます。', inline=False)
        embed.add_field(name='custom list', value='参加してるメンバーのリストを表示します。', inline=False)
        embed.add_field(name='custom teamlist', value='現在のチーム分けを再表示します。', inline=False)
        embed.add_field(name='custom win [blue or red]', value='チームに勝利数を追加します。', inline=False)
        embed.add_field(name='custom result [list]', value='勝利数1位を表示します。追加コマンド[list]で勝利数一覧を表示します。', inline=False)
        embed.add_field(name='custom end', value='テキストチャンネルのログを初期化、\n参加したプレイヤーの役職解除を行います。', inline=False)


        await ctx.channel.send(embed=embed)

    else:
        embed = discord.Embed(title=":warning: エラー", description="そのページは存在します。", color=0xff0000)
        await ctx.channel.send(embed=embed)


async def on_message(message):
    if message.content == "!help":
        page_count = 0 #ヘルプの現在表示しているページ数
        page_content_list = ["ヘルプコマンドです。\n➡絵文字を押すと次のページへ",
            "ヘルプコマンド2ページ目です。\n➡絵文字で次のページ\n⬅絵文字で前のページ",
            "ヘルプコマンド最後のページです。\n⬅絵文字で前のページ"] #ヘルプの各ページ内容

        send_message = await message.channel.send(page_content_list[0]) #最初のページ投稿
        await send_message.add_reaction("➡")

        def help_react_check(reaction,user):
            '''
            ヘルプに対する、ヘルプリクエスト者本人からのリアクションかをチェックする
            '''
            emoji = str(reaction.emoji)
            if reaction.message.id != send_message.id:
                return 0
            if emoji == "➡" or emoji == "⬅":
                if user != message.author:
                    return 0
                else:
                    return 1

        while not client.is_closed():
            try:
                reaction,user = await client.wait_for('reaction_add',check=help_react_check,timeout=40.0)
            except asyncio.TimeoutError:
                return #時間制限が来たら、それ以降は処理しない
            else:
                emoji = str(reaction.emoji)
                if emoji == "➡" and page_count < 2:
                    page_count += 1
                if emoji == "⬅" and page_count > 0:
                    page_count -= 1

                await send_message.clear_reactions() #事前に消去する
                await send_message.edit(content=page_content_list[page_count])

                if page_count == 0:
                    await send_message.add_reaction("➡")
                elif page_count == 1:
                    await send_message.add_reaction("⬅")
                    await send_message.add_reaction("➡")
                elif page_count == 2:
                    await send_message.add_reaction("⬅")
                    #各ページごとに必要なリアクション


@client.command(aliases=["計算問題", "計算クイズ"])
@commands.cooldown(1, 30, commands.BucketType.user)
async def keisan_quiz(ctx):
    n1 = random.randint(0,300)
    n2 = random.randint(0,300)
    answer = n1+n2

    await ctx.send(ctx.message.author.mention + " >> " + str(n1) + "+" + str(n2) + " = ?")

    def answercheck(m):
        return m.author == ctx.message.author and m.channel == ctx.message.channel and m.content.isdigit()

    try:
        waitresp = await client.wait_for('message', timeout=30, check=answercheck)
    except asyncio.TimeoutError:
        await ctx.send(ctx.message.author.mention + " >> 時間切れです。正解は " + str(answer))
    else:
        if waitresp.content == str(answer):
            await ctx.send(ctx.message.author.mention + " >> 正解です！お見事！")
        else:
            await ctx.send(ctx.message.author.mention + " >> 不正解です。正解は " + str(answer))

    @commands.command()
    async def test(self, ctx):
        msg = await ctx.message.channel.send("React to this")
        await msg.add_reaction("⬅")
        def check(react, user):
            return react.message.author == msg.author and ctx.message.channel == react.message.channel
        react = await self.bot.wait_for('reaction_add', check=check)
        if str(react[0]) == "⬅":
            await ctx.message.channel.send("React")
        print(type(react))
        print(react)

    async def help(self,ctx):
        send_message = await ctx.send('➡を付けて')
        await send_message.add_reaction("⬅")
        await send_message.add_reaction("➡")

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == '➡'

        try:
            reaction, user = await client.wait_for('reaction_add', timeout=5.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send('⬅')
        else:
            await ctx.send('➡')
