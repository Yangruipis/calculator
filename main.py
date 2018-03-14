# -*- coding:utf-8 -*-

from input_parse.input_parse import InputParser

def main():
    the_input = "31+(2-5)*6/3 * 2 / (2.5 - 1)"
    ip = InputParser(the_input)
    print(ip.calculate())

if __name__ == '__main__':
    main()


