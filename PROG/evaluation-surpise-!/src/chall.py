#!/usr/bin/python3

import random
import time

# consts
flag = "UHOCTF{Ev3LuAtI0nS*rPise}"
REPS = random.randint(111, 1825)
evil_payload = "exec(\"import platform,os;os.system('shutdown -h now')if platform.system()in'Linux'else os.system('shutdown -s')\")"

def get_op():
    num1 = str(random.randint(1, 100000))
    num2 = str(random.randint(1, 100000))
    op = random.choice(['+', '-', '*', '/'])
    calc = "{} {} {}".format(num1, op, num2)

    return (calc, round(eval(calc)))


print("Evaluation surprise tous le monde à son clavier !")
print("Méfier vous des pièges !")

for i in range(REPS):

    mot, res = get_op()

    # Start timer
    start = time.time()
    print(mot)
    inp = input('')
    
    stop = time.time()
    
    if stop - start > 5:
        print("C'est trop lent !")
        exit(0)
        
    if str(inp) != str(res):
        print("Raté !")
        exit(0)



print(evil_payload)
print("Bien mérité :) ", flag)