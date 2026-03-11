import string
import random

def path_cipher(text: str, key_word: str, n: int, m: int):
    """Cipher the text according to path cipher method"""
   
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    
    
    text = text.replace(" ", "")
    
    
    matrix = []
    result = ""
    
   
    for i in range(0, len(text), n):
        matrix.append(list(text[i:i+n]))
    
    
    while len(matrix[-1]) < n:
        matrix[-1].append(random.choice(alphabet))
    
    
    matrix.insert(0, list(key_word))
    
  
    sorted_indices = sorted(range(len(key_word)), key=lambda x: key_word[x])
    
    
    for col_index in sorted_indices:
        for row in matrix:
            if col_index < len(row):  
                result += row[col_index]
    
    return result


print(path_cipher(text="нельзя недооценивать противникава", key_word="пароль", n=6, m=5))