#!/usr/bin/python3

import random
import time

# consts
flag = "UHOCTF{Ev3LuAtI0nS*rPise}"
REPS = random.randint(111, 6200)

def get_op():
    num1 = str(random.randint(1, 3000))
    num2 = str(random.randint(1, 5000))
    op = random.choice(['+', '-', '*', '/'])
    
    return ("{} {} {}".format(num1, op, num2), round(eval(num1 + op + num2)))


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
        
    if inp != res:
        print("Raté !")
        exit(0)




print("Bien mérité :) ", flag)