from pynput import mouse, keyboard
import json

mouseCtl = mouse.Controller()
coords = {
    "up": {'x': 0, 'y': 44},
    "right": {'x': 0, 'y': 30},
    "down": {'x': 1051, 'y': 623},
    "left": {'x': 40, 'y': -48}
}
configFileName = "./config.json"


def on_click(x, y, button, pressed):
    if not pressed:
        print('Set at {0}'.format((x, y)))
        # Stop listener
        return False
    elif zoneToConfigure == "up":
        coords["up"]["x"] = x
        coords["up"]["y"] = y
    elif zoneToConfigure == "right":
        coords["right"]["x"] = x
        coords["right"]["y"] = y
    elif zoneToConfigure == "down":
        coords["down"]["x"] = x
        coords["down"]["y"] = y
    elif zoneToConfigure == "left":
        coords["left"]["x"] = x
        coords["left"]["y"] = y


def configure():
    global zoneToConfigure
    print("Set going [UP] zone")
    zoneToConfigure = "up"
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print("Set going [RIGHT] zone")
    zoneToConfigure = "right"
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print("Set going [DOWN] zone")
    zoneToConfigure = "down"
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print("Set going [LEFT] zone")
    zoneToConfigure = "left"
    with mouse.Listener(on_click=on_click) as listener:
        listener.join()

    print('Done configuring zones.')


def writeConfig():
    with open(configFileName, "w") as configFile:
        json.dump(coords, configFile)
        print('Configuration saved.')


def on_keyboard_release(key):
    print('Detected {0}'.format(key))
    if key == keyboard.Key.up:
        mouseCtl.position = (coords["up"]["x"], coords["up"]["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.right:
        mouseCtl.position = (coords["right"]["x"], coords["right"]["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.down:
        mouseCtl.position = (coords["down"]["x"], coords["down"]["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.left:
        mouseCtl.position = (coords["left"]["x"], coords["left"]["y"])
        mouseCtl.click(mouse.Button.left, 1)


def loadConfig():
    try:
        with open(configFileName, "r") as configFile:
            config = json.load(configFile)
            if validateConfig(config):
                setConfig(config)
                return True
            else:
                return False
    except Exception as exception:
        print("Failed reading configuration from {0}".format(configFileName))
        print(exception)
        return False


def validateConfig(config):
    errorCoords = []
    for coord in ["up", "right", "down", "left"]:
        for subCoord in ["x", "y"]:
            if config[coord][subCoord] == None:
                errorCoords.append("config.{0}.{1}".format(coord, subCoord))
    if len(errorCoords) > 0:
        print("Configuration is invalid :\n")
        for error in errorCoords:
            print("{0} invalid or not found".format(error))
        return False
    else:
        return True


def setConfig(config):
    for coord in ["up", "right", "down", "left"]:
        for subCoord in ["x", "y"]:
            coords[coord][subCoord] = config[coord][subCoord]
