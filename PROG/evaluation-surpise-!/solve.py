from pwn import *

#p = process('src/chall.py')
p = remote('localhost', 40015)


# get intial intro
w = p.recvline().decode()
w = p.recvline().decode()

op = ['+','-','*','/','%']
while True:
    w = p.recvline().decode().strip()
    print(w)
    if( any(x in w for x in op)):
        print(eval(w))
        p.sendline(str(eval(w)).encode())

