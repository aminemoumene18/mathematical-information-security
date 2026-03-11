from typing import List, Tuple

def align_numbers(u: List[int], v: List[int]) -> Tuple[List[int], List[int]]:
    n = max(len(u), len(v))
    u_aligned = [0] * (n - len(u)) + u
    v_aligned = [0] * (n - len(v)) + v
    return u_aligned, v_aligned

def remove_leading_zeros(num: List[int]) -> List[int]:
    i = 0
    while i < len(num) - 1 and num[i] == 0:
        i += 1
    return num[i:]

def big_add(u: List[int], v: List[int], b: int) -> List[int]:
    u_aligned, v_aligned = align_numbers(u, v)
    n = len(u_aligned)
    w = [0] * (n + 1)
    k = 0
    
    for j in range(n - 1, -1, -1):
        total = u_aligned[j] + v_aligned[j] + k
        w[j + 1] = total % b
        k = total // b
    
    w[0] = k
    return remove_leading_zeros(w)

def big_subtract(u: List[int], v: List[int], b: int) -> List[int]:
    u_aligned, v_aligned = align_numbers(u, v)
    n = len(u_aligned)
    w = [0] * n
    k = 0
    
    for j in range(n - 1, -1, -1):
        diff = u_aligned[j] - v_aligned[j] + k
        if diff < 0:
            w[j] = diff + b
            k = -1
        else:
            w[j] = diff
            k = 0
    
    return remove_leading_zeros(w)

def big_multiply(u: List[int], v: List[int], b: int) -> List[int]:
    m = len(u)
    n = len(v)
    w = [0] * (m + n)
    
    for j in range(n - 1, -1, -1):
        if v[j] == 0:
            continue
        
        k = 0
        for i in range(m - 1, -1, -1):
            t = u[i] * v[j] + w[i + j + 1] + k
            w[i + j + 1] = t % b
            k = t // b
        w[j] += k
    
    return remove_leading_zeros(w)

def big_divide(u: List[int], v: List[int], b: int) -> Tuple[List[int], List[int]]:
    num_u = int(''.join(str(digit) for digit in u), b)
    num_v = int(''.join(str(digit) for digit in v), b)
    
    q_num = num_u // num_v
    r_num = num_u % num_v
    
    if q_num == 0:
        q = [0]
    else:
        q_digits = []
        while q_num > 0:
            q_digits.insert(0, q_num % b)
            q_num //= b
        q = q_digits
    
    if r_num == 0:
        r = [0]
    else:
        r_digits = []
        while r_num > 0:
            r_digits.insert(0, r_num % b)
            r_num //= b
        r = r_digits
    
    return q, r

def test_arithmetic():
    print("Тест 1 (небольшие числа в десятичной системе):")
    u = [1, 2, 3]
    v = [4, 5]
    print(f"u = {u}, v = {v}")
    
    result_add = big_add(u, v, 10)
    print(f"Сложение: Результат = {result_add}")
    
    result_sub = big_subtract(u, v, 10)
    print(f"Вычитание: Результат = {result_sub}")
    
    result_mul = big_multiply(u, v, 10)
    print(f"Умножение: Результат = {result_mul}")
    
    result_div_q, result_div_r = big_divide(u, v, 10)
    print(f"Деление: Частное = {result_div_q}, Остаток = {result_div_r}")
    print()
    
    print("Тест 2 (числа с разной длиной в десятичной системе):")
    u = [9, 9, 9, 9]
    v = [2, 5]
    print(f"u = {u}, v = {v}")
    
    result_add = big_add(u, v, 10)
    print(f"Сложение: Результат = {result_add}")
    
    result_sub = big_subtract(u, v, 10)
    print(f"Вычитание: Результат = {result_sub}")
    
    result_mul = big_multiply(u, v, 10)
    print(f"Умножение: Результат = {result_mul}")
    
    result_div_q, result_div_r = big_divide(u, v, 10)
    print(f"Деление: Частное = {result_div_q}, Остаток = {result_div_r}")
    print()
    
    print("Тест 3 (деление на 1 в десятичной системе):")
    u = [7, 8, 9]
    v = [1]
    print(f"u = {u}, v = {v}")
    
    result_div_q, result_div_r = big_divide(u, v, 10)
    print(f"Деление: Частное = {result_div_q}, Остаток = {result_div_r}")
    print()
    
    print("Тест 4 (двоичная система счисления):")
    u = [1, 0, 1, 1]
    v = [1, 0, 1]
    print(f"u = {u} (двоичное), v = {v} (двоичное)")
    
    result_add = big_add(u, v, 2)
    print(f"Сложение: Результат = {result_add} (двоичное)")
    
    result_mul = big_multiply(u, v, 2)
    print(f"Умножение: Результат = {result_mul} (двоичное)")
    
    result_div_q, result_div_r = big_divide(u, v, 2)
    print(f"Деление: Частное = {result_div_q} (двоичное), Остаток = {result_div_r} (двоичное)")

if __name__ == "__main__":
    test_arithmetic()