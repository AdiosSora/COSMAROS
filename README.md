<h1>DiscordBot_SoramanNo.2</h1>
使いたい機能だけ詰め込んだDiscord用BOTです。
<h2>機能一覧</h2>
<details>
  <summary><b>一般機能</b>(開きます)　一般的な機能や、独立している機能です。</summary>
  <div style="width:90%; padding:2% 5%; border :solid 2px #bbbbbb;">
  <ul>
    <li><b>ping</b></li>「pong!」を返します
    <li><b>mention</b></li>送信者にメンションを送り返します
    <li><b>help</b></li>コマンドのヘルプを表示します。リアクションの矢印を押すことでページ遷移を可能にしています。  何もリアクションせず30秒経つとリアクションの受付を停止します。
    <li><b>role add</b></li>コマンドを入力したユーザーに役職を付与します。（そらまんランドでのみ機能します）
    <li><b>そらまん</b></li>「呼んだ？」を返します
  </ul>
  </div>
</details>
<details>
  <summary><b>カスタムマッチ機能</b>(開きます)　LoL用内戦機能</summary>
  <br>
  LoLのカスタムマッチの時のチーム振り分けや、役職を振り分けることでチャットの盗み見防止、誤ったボイスチャットへの入出を防ぐことが出来ます。<br>
  <br>
  <h3>前提</h3>
    この機能は前提として以下のテキスト、ボイスチャンネル。役職を必要としています。<br>
    ユーザーが設定する機能は後日追加予定です。<br>
    役職をそれぞれのテキストチャンネルとボイスチャンネルに割り当てることで、トラブルを防ぎます。<br>
  <br>
  <table>
    <tr>
      <th>テキストチャンネル</th>
      <th>ボイスチャンネル</th>
      <th>役職</th>
    </tr>
    <tr>
      <th>custom_general</th>
      <th></th>
      <th></th>
    </tr>
    <tr>
      <th>custom-1</th>
      <th>Custom-1</th>
      <th>Custom-1</th>
    </tr>
    <tr>
      <th>custom-2</th>
      <th>Custom-2</th>
      <th>Custom-2</th>
    </tr>
  </table>
  <ul>
    <li><b>custom start</b></li>
    「custom_general」チャンネルに入室している10名を自動的に2チームに振り分けると同時に役職を付与します。
    10名以上の場合はランダムに10名選出されます。10名以下では利用できません。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76347968-d1fd7580-634a-11ea-9e5a-a597298086ee.gif" alt="custom_start">
    </details>
    <li><b>custom suffle</b></li>
    振り分けられたチームを完全にシャッフルして再度2チームに振り分けます。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348957-7633ec00-634c-11ea-9a39-e7d1c59c2e93.gif" alt="custom_start">
    </details>
    <li><b>custom list</b></li>
    チーム関係なく10名全員のリストを表示します。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348417-81d2e300-634b-11ea-8dd2-0f0bf7dad1a6.gif" alt="custom_start">
    </details>
    <li><b>custom teamlist</b></li>
    チーム毎のメンバーリストを表示します。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348431-88f9f100-634b-11ea-8ed0-9cc662582943.gif" alt="custom_start">
    </details>
    <li><b>custom change [数字] [数字]</b></li>
    チームメンバーリスト等で表示された番号を指定することでチーム間のメンバー移動が出来ます。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76408908-09166a00-63d1-11ea-9099-c6e9c43c51d4.gif" alt="custom_start">
    </details>
    <li><b>custom win [red or blue]</b></li>
    勝利したチームを指定することでチームメンバー全員に勝利数が1追加されます。
    <li><b>custom result</b></li>
    チーム振り分け機能が終了するまでに最多の勝利数を獲得したメンバーを表示します。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348957-7633ec00-634c-11ea-9a39-e7d1c59c2e93.gif" alt="custom_start">
    </details>
    <li><b>custom end</b></li>
    振り分け機能を終了します。メンバーに付けた役職の自動解除、専用テキストチャンネルのログリセット、戦績のリセットを行います。
    <details>
      <summary>プレビュー</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348471-99aa6700-634b-11ea-83b1-16a93a4fd979.gif" alt="custom_start">
    </details>
  </ul>
</details>
<h2>Requirement</h2>
<ul>
  <li>Python3.7</li>
  <li>Discord.py</li>
  python3 -m pip install -U discord.py
  <li>GoogleカレンダーAPI</li>
  python3 -m pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
  <li>yaml</li>
  python3 -m pip install pyyaml
</ul>
<h2>Auther</h2>
<ul>
  <li>作成者：そらまん</li>
  <li>Twitter:@adiossora</li>
</ul>
<h2>License</h2>
"DiscordBot_SoramanNo.2" is under [GNU General Public License v3.0](https://en.wikipedia.org/wiki/GNU_General_Public_License)
