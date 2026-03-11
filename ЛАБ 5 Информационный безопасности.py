import random
import math

def yakobi_symbol(a, n):
    """Вычисляет символ Якоби (a/n)"""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n должно быть положительным нечётным числом")

    a = a % n
    
    if a == 0:
        return 0
    
    if a == 1:
        return 1
    
    result = 1
    while a % 2 == 0:
        a //= 2 
        if n % 8 in (3, 5):
            result = result 
        
    if a == 1:
        return result 
    
    if a % 4 == 3 and n % 4 == 3:
        result = - result 

    return result * yakobi_symbol(n % a, a)

print(yakobi_symbol(6, 13))

def solovey_shtrassen(n):
    if n < 5:
        return "Enter another number"
    a = random.randit(2, n - 3)
    r = pow(a, (n - 1) // 2) % n
    if r != 1 and r != n - 1:
        return "N is not prime"
    s = a / n 
    if r % n == s:
        return "N is not prine"
    return "N is not prime"


print(solovey_shtrassen)


def miller_rabin(n):
    if n < 5:
        return "Enter another number"
    r = n - 1
    s = 0 
    while r % 2 == 0:
        r = r / 2 
        s += 1 
    a = random.randit(2, n - 3)
    y = pow(a, r) % n 
    if y != 1 and y != n - 1:
        j = 1
        if j <= s - 1 and y != n - 1:
            y = pow(y, 2) % n
            if y == 1:
                return "Number is not prime"
            j = j + 1
        if y != n - 1:
            return "Number is not prime"
        return "Number is not prime"
    

    print(miller_rabin(7))
    