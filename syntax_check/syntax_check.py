# -*- coding:utf-8 -*-

from input_parse.stack import Stack
from utils.error import IncorrectToken, MisMatchBracket
from input_parse.token import *

def check(elements):
    stack = Stack()
    for i in elements:
        if isinstance(i, BaseToken):
            stack.push(i)


        # if isinstance(i, (int, float)):
        #     if not isinstance(stack.peak, BaseToken):
        #         raise IncorrectToken
        #     if stack.peak.token_str == ")":
        #         raise IncorrectToken
        #
        # elif isinstance(i, BaseToken):
        #     if isinstance(stack.peak, BaseToken) and stack.peak.token_str != ")":
        #         raise IncorrectToken

            if i.token_str == ")":
                while stack.peak != "(":
                    stack.pop()
                    if stack.is_empty():
                        raise MisMatchBracket
                stack.pop()

    while not stack.is_empty():
        token = stack.pop()
        if token == "(" or token == ")":
            raise MisMatchBracket


