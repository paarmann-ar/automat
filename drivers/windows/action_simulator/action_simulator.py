from typing import Any
import pyautogui
from toolboxs.delay import Delay
from toolboxs.decorators import singleton

# --
# ...
# --
@singleton
class ActionSimulator:
    def __init__(self) -> None:
        pass

    # --
    # ...
    # --

    def keyboard(self, text, delay=50, is_press_enter=True):
        Delay(1000)
        for chr in text:
            Delay(delay)
            pyautogui.press(chr)
        
        if is_press_enter:
            pyautogui.press('enter')


    # --
    # ...
    # --

    def write(self, text, delay=50, is_press_enter=True):
        Delay(1000)
        pyautogui.write(text, interval= delay/1000)

        if is_press_enter:
            pyautogui.press('enter')