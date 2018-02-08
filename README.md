<h1 align="center">
  <img alt="py-air-hockey" src="https://github.com/i96751414/py-air-hockey/raw/master/resources/images/icon.png" width="200px" height="200px"/>
  <br/>
  py-air-hockey
</h1>
<p align="center">A small Air Hockey game written in Python</p>
<div align="center">

</div>
<br/>

py-air-hockey is a cross-platform game purely written in Python. It is a very simple game developed just for fun. It has multiple game modes (single player/two players/two players over lan) and, when in single player, different difficulties: easy, medium, hard and impossible.

- **Single Player**
    Game mode where the player plays against the PC. This mode comprises 4 different difficulties, as said above.

- **Two Players**
    Play against an opponent in the same game instance, using the controls as specified bellow in [Controls](#controls) section.

- **Two Players (LAN)**
    Play against an opponent over a local area network (LAN). Therefore, each player will play on separate instances of the game.

<a name="controls"></a>
## Controls

| Key | Description |
| :--: | :-- |
| ```ARROW UP``` | Move the board up |
| ```ARROW DOWN``` | Move the board down |
| ```K``` | Move other board up ("Two Players" mode) |
| ```S``` | Move other board down ("Two Players" mode) |
| ```P``` | Pause game - same as pause button |
| ```ESC``` | Quit game when in "Single Player" or "Two Players" mode |
| ```BACKSPACE``` | Go back one level in the current menu |
| ```ENTER``` | Select menu entry |

## Requirements
In order to run py-air-hockey, the following libraries must be installed:
- [pygame](https://www.pygame.org) - "Free and Open Source python programming language library for making multimedia applications like games built on top of the excellent SDL library."
- [pygameMenu](https://github.com/ppizarror/pygame-menu) - Python library used to create menus on pygame.

You can use pip to install any missing requirements: 
```commandline
pip install -r requirements.txt
```

## Run the game
To start the game, simply run ```run.py``` file. 

Currently, there is no logging of exceptions/errors, so if you want to keep tracking of any error messages don't forget to run ```run.py``` using a terminal or redirect its output to a file.

## Screenshots

###### Main Menu
![][image-1]

###### Gameplay
![][image-2]

###### LAN Menu
![][image-3]

###### About Menu
![][image-4]

[image-1]: https://github.com/i96751414/py-air-hockey/raw/master/resources/images/main_menu.png "Main menu"
[image-2]: https://github.com/i96751414/py-air-hockey/raw/master/resources/images/gameplay.png "Gameplay"
[image-3]: https://github.com/i96751414/py-air-hockey/raw/master/resources/images/lan.png "LAN menu"
[image-4]: https://github.com/i96751414/py-air-hockey/raw/master/resources/images/about.png "About menu"
