import pyautogui
import time
import math

radius = 50  # Adjust the radius as desired
speed = 2    # Adjust the speed as desired

while True:
    for angle in range(0, 360, 10):
        x = math.cos(math.radians(angle)) * radius
        y = math.sin(math.radians(angle)) * radius
        pyautogui.moveTo(x, y, duration=speed)
        time.sleep(0.1)

