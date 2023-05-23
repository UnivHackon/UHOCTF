from pwn import *

#p = process('src/chall.py')
p = remote('localhost', 40014)

def qwert_to_azerty(texte):
    tab = {
        'q': 'a',
        'w': 'z',
        'e': 'e',
        'r': 'r',
        't': 't',
        'y': 'y',
        'u': 'u',
        'i': 'i',
        'o': 'o',
        'p': 'p',
        'a': 'q',
        's': 's',
        'd': 'd',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'z': 'w',
        'x': 'x',
        'c': 'c',
        'v': 'v',
        'b': 'b',
        'n': 'n',
        'Q': 'A',
        'W': 'Z',
        'E': 'E',
        'R': 'R',
        'T': 'T',
        'Y': 'Y',
        'U': 'U',
        'I': 'I',
        'O': 'O',
        'P': 'P',
        'A': 'Q',
        'S': 'S',
        'D': 'D',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'J': 'J',
        'K': 'K',
        'L': 'L',
        'M': 'M',
        'Z': 'W',
        'X': 'X',
        'C': 'C',
        'V': 'V',
        'B': 'B',
        'N': 'N'
    }

    t = ''
    for c in texte:
        if c in tab:
            t += tab[c]
        else:
            t += c
    return t


# get intial intro
w = p.recvline().decode()
compteur = 0

while True:
    w = p.recvline().decode().strip().replace('>','')
    print(w)
    if('Bravo' in w):
        break
    p.sendline(qwert_to_azerty(w).encode())
    compteur += 1
p.sendline(str(compteur).encode())

p.interactive()