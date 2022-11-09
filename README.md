# Dice Hero Automator (WIP)
A python script to automate grinding resources and basic gameplay in RPG Dice: Heroes of Whitestone

## Installation
### Ubuntu Linux
Open the terminal, navigate to the downloaded project folder, and install the requirements as follows
```bash
sudo apt-get install -Y python3 scrcpy android-platform-tools
python3 -m venv ./venv
source venv/bin/activate
python3 -m pip install -r requirements.txt
```

With versions of Ubuntu that use Wayland, you'll need to disable this following [this guide](https://linuxhint.com/enable-disable-wayland-ubuntu/).

## Usage
From the terminal, navigate to the project, activate the venv environment and run:
```
python3 main.py
```