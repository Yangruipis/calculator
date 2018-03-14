# -*- coding:utf-8 -*-


class EmptyStackError(IndexError):

    def __init__(self, *args):
        self.args = args


class TokenError(BaseException):

    def __init__(self, *args):
        self.args = args


class UnDefinedToken(TokenError):

    def __init__(self, *args):
        self.args = args


class IncorrectToken(TokenError):

    def __init__(self, *args):
        self.args = args


class MisMatchBracket(TokenError):

    def __init__(self, *args):
        self.args = args