このBOTが出来ること。

5vs5のカスタムマッチのサポートをすることが出来ます。

利用に必要なチャンネルと役職

voice_channels
  ・custom_general

text_channel
  ・custom-1
  ・custom-2

Role
  ・Custom-1
  ・Custom-2

コマンド

!custom start
ボイスチャンネル「custom_general」にいるユーザーを取得して
5人ずつの2チームに振り分け、役職を付与します。
10人未満だとコマンドを実行出来ません。
10人以上だと上から順に10人まで取得します。

!custom shuffle
「!custom start」を実行した後に再シャッフルを行い5:5で再度チーム分けを行います。
実行前にこのコマンドを実行してもエラーが返ってきます。

!custom end
テキストチャンネル「custom-1」と「custom-2」のチャットログをリセットし、
メンバーの役職を解除を行います。
こちらも「!custom start」を実行していないとエラーが返ってきます。

!custom change [数値1] [数値2]
start時もしくはteamlistに表示される番号を指定することで
指定した場所同士を入れ替えることが出来ます。

!custom list
メンバー全員を表示することが出来ます。

!custom teamlist
2チームの内訳を表示します
