FLAG = bytearray(b'UHOCTF{??????????????????????ng3}')
CIPHER = bytearray(b'>ZCt\xf8j\x7f9a\xe3\xdeX`9\x06\xd8\x1d73W\xe2\xfa4Qd\x03\x9d\x1d7\x02h\xe1\xd5')
#CIPHER = bytearray(b'\xa2\xbd\x7f\xbe\x1d~\x0bW\x7A\xa5\xc4\x87\x05\xcc=\tC]\xe1@\x81\xa8\xb6X\xc9x\tCl\xdeC\xae')

print(f"{CIPHER[10]}")

FLAG[7] = CIPHER[7] ^ FLAG[29] ^ CIPHER[29]
FLAG[8] = CIPHER[8] ^ FLAG[30] ^ CIPHER[30]
FLAG[9] = CIPHER[9] ^ FLAG[31] ^ CIPHER[31]
FLAG[10] = CIPHER[10] ^ FLAG[32] ^ CIPHER[32]

for i in range(11):
    FLAG[11 + i] = CIPHER[11 + i] ^ FLAG[i] ^ CIPHER[i]

for i in range(7):
    FLAG[22 + i] = CIPHER[22 + i] ^ FLAG[11 + i] ^ CIPHER[11 + i]

print(f"{FLAG}")