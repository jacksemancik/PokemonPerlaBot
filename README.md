# PokemonPerlaBot
A Bot Programmed to Play Pokemon Perla. At this current stage, the bot saves the game, and walks the player from left to right, if the pixel underneath the mouse cursor is the same color as the in-game sprite's head (i.e. if the mouse is hovered over the character). When a battle is initiated, PerlaBot presses the X key (the A Button) until the battle ends. If the switch-variable is set to `True`, then the bot switches the positions of the first and second Pokémon in the party. Currently, PerlaBot is functional in Pokemon Perla (a bootleg of Pokemon Ruby), with updates coming soon for functionality in Pokemon Ruby, Sapphire, Emerald, FireRed, LeafGreen, and ChaosBlack (a bootleg of FireRed). PerlaBot is written in Python.

It should also be noted that PerlaBot has a "failsafe" method programmed in; if you move your mouse to the upper-left corner of your computer screen, the programme will automatically stop.
## Dependencies
PerlaBot requires [PyAutoGUI](https://github.com/asweigart/pyautogui), [PyScreeze](https://github.com/asweigart/pyscreeze), and [Pillow](https://pypi.python.org/pypi/Pillow), which can all be installed using pip:
```
pip install pyautogui pyscreeze Pillow
```

For Mac OSX, PyAutoGUI requires the modules [pyobjc-core](https://pypi.python.org/pypi/pyobjc-core) and [pyobjc](https://pypi.python.org/pypi/pyobjc).

For Linux distributions, PyAutoGUI requires either [python3-xlib](https://pypi.python.org/pypi/python3-xlib) (for Python 3) or [python-xlib](https://pypi.python.org/pypi/python-xlib) (for Python 2).

Additionally, Linux distributions further require `scrot`, for pixel colour detection. `scrot` can be installed through any of the following methods:

For Debian-based distributions (Debian, Ubuntu, Linux Mint):
```
sudo apt-get install scrot 
```

For Red Hat-based distributions (CentOS, SUSE, openSUSE):
```
sudo yum install scrot
```

For Fedora:
```
sudo dnf in scrot
```

For Arch-based distributions (Arch Linux, Manjaro):
```
sudo pacman -S scrot
```

Emulator controls should be set as follows:

Computer Key | Gameboy Equivalent
--- | ---
X key | A button
Z key | B button
Enter/Return key | Start button
Up key | Up
Down key | Down
Left key | Left
Right key | Right

## Usage
PerlaBot may be activated as following:
```
python perla.py maxRunTime WaitTime SwitchVariable
```
(NOTE: the `maxRunTime` and `WaitTime` variables are in minutes, while the `SwitchVariable` is a boolean value)

## Example
```
python perla.py 20 1 True
```
In this example, the bot runs for 20 minutes after a one minute waiting period. Additionally, because the switch variable is set to `True`, the first and second Pokemon in your party are switched.

## Contribute!
If you would like to contribute to this project, clone the repository and start making pull requests! I'll review them from there. Any help is greatly appreciated!
```
git clone https://github.com/jacksemancik/PokemonPerlaBot.git
```

## License
This programme is licensed under the MIT License. For more information, [read the full license!](LICENSE)

## Author
This programme was created by John "Jack" Frank Semancik V in 2017.
