
from defs import *
from pynput import keyboard
from pathlib import Path

configPath = Path(configFileName)
if configPath.is_file():
    # file exists
    print("Configuration file {0} found. Loading configuration...".format(
        configFileName))
    if not loadConfig():
        print("Reconfiguration needed...")
        configure()
        writeConfig()
else:
    print("Configuration file {0} not found.".format(configFileName))
    configure()
    writeConfig()

listener = keyboard.Listener(
    # on_press=on_press,
    on_release=on_keyboard_release)
listener.start()

input('--- Press ENTER to stop ---\n')
