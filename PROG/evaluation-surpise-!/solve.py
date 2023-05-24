from pwn import *

#p = process('src/chall.py')
p = remote('localhost', 40015)


# les lignes de bienvenue
w = p.recvline().decode()
w = p.recvline().decode()

op = ['+','-','*','/','%']

while True:
    w = p.recvline().decode().strip()
    # Vérifier si il y a un opérateur
    r = [x for x in w.split(' ') if x in op]
    if(len(r) == 1 ):
        print(eval(w))
        p.sendline(str(round(eval(w))).encode())
    else:
        print(str(w))