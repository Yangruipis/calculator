# -*- coding:utf-8 -*-

"""
解析输入的字符串
"""

from syntax_check.syntax_check import check
from .token import *
from .stack import *

class InputParser:

    def __init__(self, line: str):
        self.line = line.strip().replace(" ", "")
        self.elements = []
        self.postfix = []
        self.read_line()
        check(self.elements)
        self.transfer_postfix()

    def read_line(self):
        i, j = 0, 0
        for i, s in enumerate(self.line):
            if s in ["+", "-", "*", "/", "(", ")"]:
                if j < i:
                    self.elements.append(float(self.line[j:i]))
                self.elements.append(BaseToken(s))
                j = i+1
        if j < len(self.line):
            self.elements.append(float(self.line[j:]))

    def transfer_postfix(self):
        stack = Stack()
        for i in self.elements:
            if isinstance(i, (int, float)):
                self.postfix.append(i)
            else:
                if i.token_str == ")":
                    while stack.peak.token_str != "(":
                        self.postfix.append(stack.pop())
                    stack.pop()
                else:
                    if not stack.is_empty():
                        while i.compare(stack.peak) <= 0 and stack.peak.token_str != "(":
                            self.postfix.append(stack.pop())
                    stack.push(i)
        while not stack.is_empty():
            self.postfix.append(stack.pop())

    def calculate(self):
        stack = Stack()
        for i in self.postfix:
            if isinstance(i, (int, float)):
                stack.push(i)
            else:
                a = stack.pop()
                b = stack.pop()
                c = i.calculate(b, a)
                stack.push(c)
        return stack.peak





