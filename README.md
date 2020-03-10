
# DiscordBot_Soraman
　使いたい機能だけ詰め込んだDiscord用BOTです。

## 実装済み機能
prefix(コマンドの頭に付ける文字)は「#」を設定しています。  
### 一般機能

     一般的な機能や、独立している機能です。  

* ping   
`「pong!」を返します。`
* mention
`送信者にメンションを送り返します。`
* help 
`コマンドのヘルプを表示します。リアクションの矢印を押すことでページ遷移を可能にしています。  何もリアクションせず30秒経つとリアクションの受付を停止します。`
* role add 
`コマンドを入力したユーザーに役職を付与します。（そらまんランドでのみ機能します）`
* そらまん 
`「呼んだ？」を返します。`
***
### カスタムマッチ機能(内戦機能)
LoLのカスタムマッチの時のチーム振り分けや、役職を振り分けることでチャットの盗み見防止、誤ったボイスチャットへの入出を防ぐことが出来ます。  
### 前提

    この機能は前提として以下のテキスト、ボイスチャンネル。役職を必要としています。  
    ユーザーが設定する機能は後日追加予定です。  
    役職をそれぞれのテキストチャンネルとボイスチャンネルに割り当てることで、トラブルを防ぎます。  

| テキストチャンネル | ボイスチャンネル | 役職 |
|--|--|--|
| custom_general |  |  |
| custom-1 | Custom-1 | Custom-1 |
| custom-2 | Custom-2 | Custom-2 |
 - custom start  
 `「custom_general」チャンネルに入室している10名を自動的に2チームに振り分けると同時に役職を付与します。10名以上の場合はランダムに10名選出されます。10名以下では利用できません。`  
![custom_start](https://user-images.githubusercontent.com/11624644/76347968-d1fd7580-634a-11ea-9e5a-a597298086ee.gif)
 - custom suffle
 ``
![custom_shuffle](https://user-images.githubusercontent.com/11624644/76348957-7633ec00-634c-11ea-9a39-e7d1c59c2e93.gif)
 - custom list
 ``
![custom_list](https://user-images.githubusercontent.com/11624644/76348417-81d2e300-634b-11ea-8dd2-0f0bf7dad1a6.gif)
 - custom teamlist
 ``
![custom_teamlist](https://user-images.githubusercontent.com/11624644/76348431-88f9f100-634b-11ea-8ed0-9cc662582943.gif)
 - custom change [数字] [数字]
 ``
 - custom win [red or blue]
 ``
 - custom result
 ``
![custom_win_and_result](https://user-images.githubusercontent.com/11624644/76349186-e17dbe00-634c-11ea-968f-da8eb58bb81d.gif)
 - custom end
 ``
![custom_end](https://user-images.githubusercontent.com/11624644/76348471-99aa6700-634b-11ea-83b1-16a93a4fd979.gif)
## 使用パッケージ
* *Discord.py*  
  *  `python3 -m pip install -U discord.py`  
* *GoogleカレンダーAPI*  
  *  `python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`  
* *yaml*  
  *  `pip install pyyaml`  
