def generateKey(plain_text: str, key: str) -> str:
    key = list(key)
    if len(plain_text) == len(key):
        return key
    elif len(plain_text) < len(key):
        new_key: list[str] = []
        for i in range(len(plain_text)):
            new_key.append(key[i])
        return new_key
    else:
        for i in range(len(plain_text) - len(key)):
            key.append(key[i])
        return key
def cipherText(plain_text: str, key: str) -> str:
    cipher: list[str] = []
    for i in range(len(plain_text)):
        cipher.append(chr(((ord(key[i]) + ord(plain_text[i])) % 26)+ ord('A')))
    return ("".join(cipher))
def ogText(cipher: str, key: str) -> str:
    og: list[str] = []
    for i in range(len(key)):
        og.append(chr(((ord(cipher[i]) - ord(key[i]) + 26) % 26) + ord('A')))
    return ("".join(og))

print("-------vigenere-cipher-------")
while True:
    choice: str = input("Encrypt/Decrypt/Exit (E/D/X): ").upper()
    if choice == 'E':
        plain: str = input("Plain Text: ").upper()
        keyword: str = input("Key: ").upper()
        key = generateKey(plain,keyword)
        cipher = cipherText(plain,key)
        print(cipher)
    elif choice == 'D':
        cipher: str = input("Cipher Text: ").upper()
        keyword: str = input("Key: ").upper()
        key = generateKey(cipher,keyword)
        og = ogText(cipher,key)
        print(og)
    elif choice == 'X':
        exit()
    else:
        print("Wrong Input!!")
