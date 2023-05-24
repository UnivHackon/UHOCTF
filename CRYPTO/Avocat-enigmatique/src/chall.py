flag = "La plaidoirie avocatiale est un art subtil"

def encode(ciphertext):
    return "".join([chr(ord(c) + 0x0A) if c.isalpha() else c for c in ciphertext])

# a = 97 k = 107
# A = 65 K = 75

if __name__ == "__main__":
    print(f'{encode(flag)}')