flag = "La plaidoirie avocatiale est un art subtil"

def encode(ciphertext):
    print(ord('a'), ord('A'), ord('k'), ord('K'))
    return "".join([chr(ord(c) + 0x0A) if c.isalpha() else c for c in ciphertext])

if __name__ == "__main__":
    print(f'{encode(flag)}')