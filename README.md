
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
<details> <summary> プレビュー </summary> <div> ![custom_start](https://user-images.githubusercontent.com/11624644/76347968-d1fd7580-634a-11ea-9e5a-a597298086ee.gif)</div> </details>
 - custom suffle
 ``
<details> <summary> プレビュー </summary> <div> ![](https://user-images.githubusercontent.com/11624644/76347614-44ba2100-634a-11ea-9239-c420f2d588a7.gif) </div> </details>
 - custom list
 ``
<details> <summary> プレビュー </summary> <div> ![enter image description here](https://user-images.githubusercontent.com/11624644/76347612-44218a80-634a-11ea-9134-5c2d6004e1d2.gif) </div> </details>
 - custom teamlist
 ``
<details> <summary> プレビュー </summary> <div> ![enter image description here](https://user-images.githubusercontent.com/11624644/76347618-4552b780-634a-11ea-814d-4a38252033d9.gif) </div> </details>
 - custom change [数字] [数字]
 ``
<details> <summary> プレビュー </summary> <div> ![enter image description here](https://user-images.githubusercontent.com/11624644/76347604-42f05d80-634a-11ea-9970-e5d12b2b6981.gif) </div> </details>
 - custom win [red or blue]
 ``
 - custom result
 ``
<details> <summary> プレビュー </summary> <div> ![enter image description here](https://user-images.githubusercontent.com/11624644/76347619-45eb4e00-634a-11ea-8354-66cc59559c06.gif) </div> </details>
 - custom end
 ``
<details> <summary> プレビュー </summary> <div> ![enter image description here](https://user-images.githubusercontent.com/11624644/76347610-44218a80-634a-11ea-9895-a457dc3ba6f8.gif) </div> </details>

## 使用パッケージ
* *Discord.py*  
  *  `python3 -m pip install -U discord.py`  
* *GoogleカレンダーAPI*  
  *  `python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`  
* *yaml*  
  *  `pip install pyyaml`  
