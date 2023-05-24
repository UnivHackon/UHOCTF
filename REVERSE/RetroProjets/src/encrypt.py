FLAG = "UHOCTF{Inspiration_From_The_Past}"

def CaesarCipher(flag):
    cipher = ""
    for i in range(len(flag)):
        char = flag[i]
        if not char.isalpha():
            cipher += char
        elif char.isupper():
            cipher += chr((ord(char) + 13 - 65) % 26 + 65)
        else:
            cipher += chr((ord(char) + 13 - 97) % 26 + 97)
    return cipher

def ReverseCipher(flag):
    cipher = ""
    for i in range(len(flag)):
        cipher += flag[len(flag) - i - 1]
    return cipher[::-1]

def main():
    print(f"CaesarCipher: {CaesarCipher(FLAG), len(CaesarCipher(FLAG))}")
    print(f"ReverseCipher: {ReverseCipher(FLAG)}")

if __name__ == "__main__":
    main()