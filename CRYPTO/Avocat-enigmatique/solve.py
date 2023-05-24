def decrypt(message):
    decrypted = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted += chr((ord(char) - 65 - 10) % 26 + 65)
            else:
                decrypted += chr((ord(char) - 97 - 10) % 26 + 97)
        else:
            decrypted += char
    return decrypted

print(decrypt("Vk zvksnys|so kymk~skvo o}~ x k|~ }l~sv"))