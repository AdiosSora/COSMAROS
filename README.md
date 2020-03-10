# DiscordBot_Soraman
　使いたい機能だけ詰め込んだDiscord用BOTです。

## 実装済み機能
prefix(コマンドの頭に付ける文字)は「#」を設定しています。  
### 一般機能
一般的な機能や、独立している機能です。  
* ping 「pong!」を返します。
* mention 送信者にメンションを送り返します。  
* help コマンドのヘルプを表示します。リアクションの矢印を押すことでページ遷移を可能にしています。  何もリアクションせず30秒経つとリアクションの受付を停止します。
* role add コマンドを入力したユーザーに役職を付与します。（そらまんランドでのみ機能します）
* そらまん 「呼んだ？」を返します。
### カスタムマッチ機能(内戦機能)
LoLのカスタムマッチの時のチーム振り分けや、役職を振り分けることでチャットの盗み見防止、誤ったボイスチャットへの入出を防ぐことが出来ます。  
#### 前提
この機能は前提として以下のテキスト、ボイスチャンネル。役職を必要としています。  
ユーザーが設定する機能は後日追加予定です。  
役職をそれぞれのテキストチャンネルとボイスチャンネルに割り当てることで、トラブルを防ぎます。  
* テキストチャンネル
  * custom_general
  * custom-1
  * custom-2
* ボイスチャンネル
  * Custom-1
  * Custom-2
* 役職
  * Custom-1
  * Custom-2
* !custo


## 使用パッケージ
* *Discord.py*  
  *  `python3 -m pip install -U discord.py`  
* *GoogleカレンダーAPI*  
  *  `python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`  
* *yaml*  
  *  `pip install pyyaml`  
