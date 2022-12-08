import os
import sys
import re

from lexer import Lexer

Lexer = Lexer()


def main():
    # Reads the file with the code
    a = []
    with open("TestFiles/Test1.txt", encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                a.append(word)

    # print(a)
    Lexer.token(a)


main()
