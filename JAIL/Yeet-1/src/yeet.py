#!/bin/python3

import re

flag = open('flag.txt').read()

inp = input('> ')

if  re.search(r'\_',inp) or re.search(r'\d', inp) or eval(inp) != 9580:
    print('Nope')
else:
    print(flag)