<div align="center">
<img width="60%" src="https://user-images.githubusercontent.com/11624644/79453042-1227d600-8024-11ea-83ad-42f799b0eade.png" alt="COSMAROS"><br>
<img src="https://img.shields.io/badge/-Python-F9DC3E.svg?logo=python&style=flat">
<img src="https://img.shields.io/badge/-Discord-f0b686.svg?logo=discord&style=flat">
<a href="https://en.wikipedia.org/wiki/GNU_General_Public_License"><img src="http://img.shields.io/badge/license-GPL-blue.svg?style=flat" alt="GNU_General_Public_License"></a>
<img src="https://img.shields.io/badge/version-v0.9.0-ff7964.svg" alt="version">
</div>
<h1>COSMAROS</h1>
COSMAROS is a discord BOT that is packed with only the functions you want to use for now. <br>
When you are fighting a civil war in LoL, it will automatically prevent you from being notified of the other party's chat<br>.
We came up with the idea of assigning roles and dividing teams, which would be great. <br>
I also wanted to be able to refer to the LoL information from Discord. <br>


<h2>How to Use</h2>
Please click on the following URL to add the BOT to the server.<br>
https://discordapp.com/oauth2/authorize?client_id=477820647414824961&scope=bot&permissions=0

<h2>Function</h2>
<details>
  <summary><b>general function</b>(open)It is a general feature or a stand-alone feature.</summary>
  <ul>
    <li><b>ping</b></li>「pong!to return
    <li><b>mention</b></li>Mentions are sent back to the sender.
    <li><b>help</b></li>Displays help for the command. Page transitions are made possible by pressing the reaction arrow.  After 30 seconds without any reaction, the reaction will be stopped.
    <li><b>role add</b></li>Assigns a position to the user who entered the command.(It only works in Soloman Land.)
    <li><b>そらまん</b></li>「呼んだ？」to return
  </ul>
</details>
<details>
  <summary><b>Custom Match Function</b>(open)　Custom Match Function for LoL</summary>
  <br>
  You can prevent eavesdropping on the chat by assigning teams and positions during custom matches in LoL, and prevent accidental entry and exit of voice chat.<br>
  <br>
  <h3>premise</h3>
  This feature is premised on the following text, voice channels. Position needed. <br>
  More user-configurable features will be added at a later date. <br>
  Assigning roles to their own text and voice channels will save you trouble. <br>
  <br>
  <table>
    <tr>
      <th>textchannel</th>
      <th>voicechannel</th>
      <th>role</th>
    </tr>
    <tr>
      <th></th>
      <th>custom_general</th>
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
    10 people in the "custom_general" voice channel will be automatically assigned to 2 teams and given a position at the same time.
    If there are more than 10 people, 10 people will be selected at random; no more than 10 people will be available.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76347968-d1fd7580-634a-11ea-9e5a-a597298086ee.gif" alt="custom_start">
    </details>
    <li><b>custom suffle</b></li>
    Completely shuffle the assigned teams and assign them to the two teams again.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348957-7633ec00-634c-11ea-9a39-e7d1c59c2e93.gif" alt="custom_start">
    </details>
    <li><b>custom list</b></li>
    View a list of all 10 members, regardless of team.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348417-81d2e300-634b-11ea-8dd2-0f0bf7dad1a6.gif" alt="custom_start">
    </details>
    <li><b>custom teamlist</b></li>
    Displays a list of members by team.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348431-88f9f100-634b-11ea-8ed0-9cc662582943.gif" alt="custom_start">
    </details>
    <li><b>custom change [number] [number]</b></li>
    You can move members between teams by specifying the number displayed in the team member list.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76408908-09166a00-63d1-11ea-9099-c6e9c43c51d4.gif" alt="custom_start">
    </details>
    <li><b>custom win [red or blue]</b></li>
    By specifying the winning team, all team members will receive an additional 1 win.
    <li><b>custom result</b></li>
    Shows the members with the most wins by the end of the team allocation function.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348957-7633ec00-634c-11ea-9a39-e7d1c59c2e93.gif" alt="custom_start">
    </details>
    <li><b>custom end</b></li>
    Ends the sorting function. Auto-removal of the position assigned to the member, log reset of the dedicated text channel, and reset of the battle record.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76348471-99aa6700-634b-11ea-83b1-16a93a4fd979.gif" alt="custom_start">
    </details>
  </ul>
</details>
<details>
  <summary><b>League of Legends</b>(open)　User information, win rates, etc.</summary>
  <ul>
    <li>lol status <Summoner Name></li>
    The summoner's name, level, and current ranked battle tier are displayed.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76987294-49a05580-6986-11ea-9dc6-68e75b2a248d.gif" alt="custom_start">
    </details>
  </ul>
  <ul>
    <li>lol free</li>
    View the free champions available for free this week.
    <details>
      <summary>preview</summary>
      <img width="80%" src="https://user-images.githubusercontent.com/11624644/76987292-486f2880-6986-11ea-8376-91684fd61bf6.gif" alt="custom_start">
    </details>
  </ul>
</details>

<h2>Requirement</h2>
<ul>
  <li>Python3.7</li>
  <li>Discord.py</li>
  python3 -m pip install -U discord.py
  <li>yaml</li>
  python3 -m pip install pyyaml
  <li>cv2</li>
  <li>lxml</li>
  <li>riotwatcher</li>
</ul>
<h2>Auther</h2>
<ul>
  <li>作成者：そらまん</li>
  <li>Twitter:@adiossora</li>
</ul>
<h2>License</h2>
"DiscordBot_SoramanNo.2" is under [GNU General Public License v3.0](https://en.wikipedia.org/wiki/GNU_General_Public_License)
