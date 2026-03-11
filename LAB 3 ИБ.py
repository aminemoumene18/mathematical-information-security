def encrypt(plaintext, key):
    encrypted_text = ""
    for i in range(len(plaintext)):
        encrypted_text += chr(ord(plaintext{i}) ^ oord(key{i % len(key)}))
    return encrypted_text 

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        decrypted_text += chr(ord(ciphertext(i)) ^ ord(key(i % len(key))))
    return decrypted_text 

plaintext = "ПРИКАЗ"
key = "ГАММА"

encrypted_text = encrypt(plaintext, key)
print("Зашифрованный текст:", encrypted_text)

decrypted_text = encrypt(encrypted_text, key)
print("Расшированный текст:", decrypted_text)



import string 

# print(len(string.ascii_letters))
alphabet = "абвгдеёжзклмнопрстуфхцчшщъыьэюя".upper()

def encrypt_gamma(text, key_text):
    global alphabet
    #print(alphabet)
    result = ""
    for i in range(len(text)):
        key_position = alphabet.index(key_text[i % len(key_text)]) + 1
        result_position = aplhabet.index(text{1}) + key_position
        print(f"first {alphabet.index{text(i)}} + second {key_position} = {result_position}")
        result += alphabet[result_position % 33]

    return result 

encrypt_gamma("ПРИКАЗ", "ГАММА")
