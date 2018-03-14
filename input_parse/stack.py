# -*- coding:utf-8 -*-

"""
实现栈
"""

from utils.error import EmptyStackError


class Stack:

    def __init__(self):
        self.element = []
        self._length = 0
        self.clear()

    def clear(self):
        self.element = []
        self._length = 0

    def is_empty(self):
        if self.len == 0:
            return True
        return False

    @property
    def peak(self):
        if self.len == 0:
            raise EmptyStackError
        return self.element[0]

    def push(self, value):
        self.element.insert(0, value)
        self._length += 1

    @property
    def len(self):
        return self._length

    def pop(self):
        if self.is_empty():
            raise EmptyStackError
        self._length -= 1
        return self.element.pop(0)
