flag = "La plaidoirie avocatiale est un art subtil"

def encode(ciphertext):
    return "".join([ chr((ord(c) - 65 - 10) % 26 + 65) if c.isupper() else chr((ord(c) - 97 - 10) % 26 + 97) if c.isalpha() else c for c in ciphertext])

if __name__ == "__main__":
    print(f'{encode(flag)}')