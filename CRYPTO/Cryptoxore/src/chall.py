from os import urandom

FLAG = open('flag.txt', 'rb').read()
assert len(FLAG) == 33

# Convert FLAG into a list of bytes
FLAG = bytearray(FLAG)

for _ in range(32):
    for i, c in enumerate(urandom(11) * 3):
        FLAG[i] ^= c

print(f"{FLAG}")

