#!/usr/bin/python3

import random
import time

# consts
flag = "UHOCTF{LeS_cL4vIeRs_c'3sT_pQs_f4c1l3_S8R_Z1Nd3UBE!}"
REPS = random.randint(111, 6200)

def azerty_to_qwerty(texte):
    tab = {
        'a': 'q',
        'z': 'w',
        'e': 'e',
        'r': 'r',
        't': 't',
        'y': 'y',
        'u': 'u',
        'i': 'i',
        'o': 'o',
        'p': 'p',
        'q': 'a',
        's': 's',
        'd': 'd',
        'f': 'f',
        'g': 'g',
        'h': 'h',
        'j': 'j',
        'k': 'k',
        'l': 'l',
        'm': 'm',
        'w': 'z',
        'x': 'x',
        'c': 'c',
        'v': 'v',
        'b': 'b',
        'n': 'n',
        'A': 'Q',
        'Z': 'W',
        'E': 'E',
        'R': 'R',
        'T': 'T',
        'Y': 'Y',
        'U': 'U',
        'I': 'I',
        'O': 'O',
        'P': 'P',
        'Q': 'A',
        'S': 'S',
        'D': 'D',
        'F': 'F',
        'G': 'G',
        'H': 'H',
        'J': 'J',
        'K': 'K',
        'L': 'L',
        'M': 'M',
        'W': 'Z',
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

def pickRandomWord():
    w = random.choice(word)
    # Rajout des maj aléatoirement
    for l in w:
        if random.randint(0, 1) == 1:
            w = w.replace(l, l.upper(), 1)
    return w

# print intro
print("Corrige moi les mots et je te donnerai le flag !")
wordlist = open("wordlist.txt", "r")
word = [x.strip() for x in wordlist.readlines()]

for i in range(REPS):
    mot = pickRandomWord()
    ciphered = azerty_to_qwerty(mot)
    
    print(ciphered)
    
    # Start timer
    start = time.time()
    
    inp = input('>')
    
    stop = time.time()
    
    if stop - start > 5:
        print("Trop long !")
        exit(0)
        
    if inp != mot:
        print("Raté !")
        exit(0)

print("Bravo ! Combien de mots as-tu corrigé ?")
inp = input('>')
if int(inp) != REPS:
    print("Raté !")
    exit(0)


print("Bien mérité :)", flag)