import pyautogui
import sys
import time
from pynput import mouse, keyboard

leftCoords = {'x': 40, 'y': -48}
rightCoords = {'x': 0, 'y': 30}
upCoords = {'x': 0, 'y': 44}
downCoords = {'x': 1051, 'y': 623}
ACTION_TIME_SEC = 1
isConfiguring = True
zoneToConfigure = "up"
# keyboardCtl = keyboard.Controller()
mouseCtl = mouse.Controller()


# def on_move(x, y):
# print('Pointer moved to {0}'.format((x, y)))


def on_click(x, y, button, pressed):
    if not pressed:
        print('Set at {0}'.format((x, y)))
        # Stop listener
        return False
    elif zoneToConfigure == "up":
        upCoords["x"] = x
        upCoords["y"] = y
    elif zoneToConfigure == "right":
        rightCoords["x"] = x
        rightCoords["y"] = y
    elif zoneToConfigure == "down":
        downCoords["x"] = x
        downCoords["y"] = y
    elif zoneToConfigure == "left":
        leftCoords["x"] = x
        leftCoords["y"] = y


while isConfiguring:
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

    isConfiguring = False

print('Done configuring zones.')


def on_release(key):
    print('Detected {0}'.format(key))
    if key == keyboard.Key.up:
        mouseCtl.position = (upCoords["x"], upCoords["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.right:
        mouseCtl.position = (rightCoords["x"], rightCoords["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.down:
        mouseCtl.position = (downCoords["x"], downCoords["y"])
        mouseCtl.click(mouse.Button.left, 1)
    elif key == keyboard.Key.left:
        mouseCtl.position = (leftCoords["x"], leftCoords["y"])
        mouseCtl.click(mouse.Button.left, 1)


listener = keyboard.Listener(
    # on_press=on_press,
    on_release=on_release)
listener.start()

input('--- Press ENTER to stop ---\n')
