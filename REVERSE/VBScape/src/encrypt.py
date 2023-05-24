import random
from sympy import symbols, Eq, solve

delim = '/'
op_symbols = ['*', '-', '+']

MAX = 100000
MIN = 10000

def get_random_number():
    return random.randint(MIN, MAX)

def get_random_op():
    return random.choice(op_symbols)

def generate_equations(char):
    op = get_random_op()
    num1 = get_random_number()

    if op == '+':
        num2 = char - num1
    elif op == '*':
        num2 = char / num1
    elif op == '-':
        num2 = num1 + char
    else:
        raise Exception("Invalid operator")

    return f"{num2}{op}{num1}"

SOURCE = open("./source.vbs", "r").read()

def main():
    # For each character in the source code, generate an equation
    with open("encrypted.txt", "w") as f:
        f.write(f"{delim}".join([generate_equations(ord(char)) for char in SOURCE]))

if __name__ == "__main__":
    main()