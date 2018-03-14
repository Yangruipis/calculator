# -*- coding:utf-8 -*-

"""
解析符号，并且实现优先级的compare方法
+, -, *, /, (, )
"""
from utils.error import UnDefinedToken, IncorrectToken


LEVEL = {
    "+": 0,
    "-": 0,
    "*": 1,
    "/": 1,
    "(": 2,
    ")": 2
}


class BaseToken:

    def __init__(self, token_str):
        self.token_str = token_str
        self.level = 0
        self.check_input()
        self._get_level()

    def _get_level(self):
        self.level = LEVEL[self.token_str]

    def check_input(self):
        if self.token_str not in LEVEL:
            raise UnDefinedToken

    def compare(self, b):
        if self.level < b.level:
            return -1
        elif self.level > b.level:
            return 1
        else:
            return 0

    def calculate(self, a, b):
        if self.token_str in ["(", ")"]:
            raise IncorrectToken
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            if self == "+":
                return a + b
            elif self == "-":
                return a - b
            elif self == "*":
                return a * b
            elif self == "/":
                return a / b
            else:
                raise IncorrectToken
        else:
            raise TypeError

    def __eq__(self, other):
        if self.token_str == other:
            return True
        return False
