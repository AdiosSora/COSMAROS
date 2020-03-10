
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
<details> <summary> 見出し部分。ここをクリック。 </summary> <div> ここが隠れてる部分。 </div> </details>
 - custom start 
 `「custom_general」チャンネルに入室している10名を自動的に2チームに振り分けると同時に役職を付与します。10名以上の場合はランダムに10名選出されます。10名以下では利用できません。`
 - custom suffle
 - custom list
 - custom teamlist
 - custom change [数字] [数字]
 - custom win [red or blue]
 - custom result
 - custom end

## 使用パッケージ
* *Discord.py*  
  *  `python3 -m pip install -U discord.py`  
* *GoogleカレンダーAPI*  
  *  `python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`  
* *yaml*  
  *  `pip install pyyaml`  
