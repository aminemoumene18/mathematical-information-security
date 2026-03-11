import string 

alphabet =list(string.ascii_uppercase)
# print(alphabet)

# print(alphabet)
def cesar_cipher(k, text):
    ciphered_text = ""
    for letter in text:
        location = alphabet.index(letter)
        location += k 
        ciphered_text += alphabet[location % 26]
    return ciphered_text 

cesar_cipher(3, "YZZ")


import string

alphabet =list(string.ascii_uppercase)
alphabet += [" "]

print(alphabet)
def atbash_cipher(text):
    global alphabet 
    text = list(text)
    # print(text)
    """AAB - > Z """
    locations = []
    for i in text:
        locations.append(alphabet.index(i))
    result = ""
    alphabet.reverse()
    print(alphabet)
    for j in locations:
        result += alphabet[j]

    return result 

atbash_cipher("EEE AF")


    