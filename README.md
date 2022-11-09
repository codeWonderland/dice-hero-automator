# Dice Hero Automator (WIP)
A python script to automate grinding resources and basic gameplay in RPG Dice: Heroes of Whitestone

## Installation
### Ubuntu Linux
Open the terminal, navigate to the downloaded project folder, and install the requirements as follows
```bash
sudo apt-get install -Y python3 scrcpy android-platform-tools xte xdotools xwininfo
python3 -m venv ./venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

With versions of Ubuntu that use Wayland, you'll need to disable this following [this guide](https://linuxhint.com/enable-disable-wayland-ubuntu/).

## Usage
This is meant to work with an android phone. Please turn on developer mode and enable USB Debugging prior to start.

Open a terminal with your phone connected to your device and run `scrcpy`. This should give you a copy of your screen you can interact with on your computer. Navigate to the map view to start

The first time you use `scrcpy`, you may have issues getting your phone screen to display. Try using `adb kill-server` to reset the connection, approve the connection via the pop-up on your phone, and run the `scrcpy` command again.

Open a new terminal terminal, navigate to the project, activate the venv environment and run:
```
python3 main.py
```

## Customizations
This project is fully set up to grab a screen capture and parse it based on the priorities file. To figure out percentages and colors necessary to make changes to the priorities file, go to the `main.py` file and turn on `test_mode` or `admin_mode` using the function defaults for `start_game()`