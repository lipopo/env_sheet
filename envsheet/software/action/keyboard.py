from pynput.keyboard import Key, Controller

from envsheet.software.action.base import BaseActionController


class KeyboardActionController(BaseActionController):

    action = [
        "keypress",
        "keyrelease",
        "click"
    ]

    def __init__(self):
        # 获取keyboard控制权
        self.keyboard = Controller()

    def get_key(self, keyname):
        if keyname == "space":
            return Key.space
        elif keyname == "left":
            return Key.left
        ...

    def do(self, action, keyname):
        """
        执行动作
        """
        key = self.get_key(keyname)
        if action == "keypress":
            self.keyboard.press(key)
        elif action == "keyrelease":
            self.keyboard.release(key)
        elif action == "click":
            self.keyboard.press(key)
            self.keyboard.release(key)