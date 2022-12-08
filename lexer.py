# from parser import *

# parser = RDA(1)

class Lexer:
    array = []
    tokenList = [
        'id',
        'FINISH',
        'BEGIN',
        'iffy',
        'loop',
        '+',
        '-',
        '*',
        '/',
        '%',
        '>',
        '<',
        '>=',
        '<=',
        '=',
        '!=',
        '{',
        '}',
        'int_lit',
        'float_lit',
        'OR',
        'AND',
        'bool_lit'
    ]

    def token(self, input1):
        self.array
        tokenList = self.tokenList

        array = [x for x in input1 if x in tokenList]
        print(array)
        print("Total number of tokens = ")
        print(len(array))