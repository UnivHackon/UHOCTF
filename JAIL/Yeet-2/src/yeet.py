#!/bin/python3

import re

flag = open('flag.txt').read()

inp = input('> ')

if  re.search(r'[123456789]', inp) or re.search(r'\_',inp) or re.search(r'\(', inp) or eval(inp)  != 9580:
    print(inp)
    print('Nope')
else:
    print(flag)