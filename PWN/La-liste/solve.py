from pwn import *


# run the process locally
p = process('./calculateur_express')


op = ['+','-','*','/']
i = 0

while True:
    w = p.recvline().decode().strip()

    if 'flag' in w:
        print(w)
        break
    if '?' not in w:
        continue

    i += 1
    w = w.split('=')
    res = w[1]
    w = w[0]

    p.recvuntil(b'>')

    for x in op:
        if (round(float(eval(w.replace('?', x))), 2) == float(res)):
            print(f"{i} | {w.replace('?', x)} = {float(res)}")
            p.sendline(x.encode())
            continue

