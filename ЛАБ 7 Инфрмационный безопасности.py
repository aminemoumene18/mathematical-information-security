import random
from math import gcd


def pollard_rho_dlog(p: int, a: int, b: int, r: int, max_iter: int = 10000) -> int:
    """
    Алгоритм Полларда (ро-метод) для решения задачи дискретного логарифма: 
    Найти x такой, что a^x ≡ b (mod p), где порядок a равен r.
    """
    
    def f(state: tuple, p: int, a: int, b: int, r: int) -> tuple:
        """Функция итерации для метода Полларда"""
        x, alpha, beta = state
        
        if x % 3 == 0:
            
            return ((x * b) % p, alpha, (beta + 1) % r)
        elif x % 3 == 1:
            
            return ((x * x) % p, (2 * alpha) % r, (2 * beta) % r)
        else:
            
            return ((x * a) % p, (alpha + 1) % r, beta)

    
    state1 = (1, 0, 0)  
    state2 = (1, 0, 0)  

    for i in range(max_iter):
        
        state1 = f(state1, p, a, b, r)

        
        state2 = f(state2, p, a, b, r)
        state2 = f(state2, p, a, b, r)

        
        if state1[0] == state2[0]:  
            x1, alpha1, beta1 = state1
            x2, alpha2, beta2 = state2
            
            
            
            
            

            delta_alpha = (alpha1 - alpha2) % r
            delta_beta = (beta2 - beta1) % r

            if delta_beta == 0:
                
                continue

            
            g = gcd(delta_beta, r)
            
            if g == 1:
                
                inv_delta_beta = pow(delta_beta, -1, r)
                x_candidate = (delta_alpha * inv_delta_beta) % r
                
                
                if pow(a, x_candidate, p) == b:
                    return x_candidate
            else:
                
                if delta_alpha % g != 0:
                    
                    continue
                
                
                delta_beta_prime = delta_beta // g
                r_prime = r // g
                delta_alpha_prime = delta_alpha // g
                
                
                inv_delta_beta_prime = pow(delta_beta_prime, -1, r_prime)
                x0 = (delta_alpha_prime * inv_delta_beta_prime) % r_prime
                
                
                for k in range(g):
                    x_candidate = (x0 + k * r_prime) % r
                    if pow(a, x_candidate, p) == b:
                        return x_candidate

    raise ValueError(f"Коллизия не найдена за {max_iter} итераций")


def verify_dlog(p: int, a: int, b: int, x: int) -> bool:
    """
    Проверка корректности вычисленного дискретного логарифма
    """
    return pow(a, x, p) == b



if __name__ == "__main__":
    p = 107
    a = 10
    b = 64
    r = 53  

    print(f"Параметры задачи:")
    print(f"p = {p} (порядок группы)")
    print(f"a = {a} (основание)")
    print(f"b = {b} (значение)")
    print(f"r = {r} (порядок элемента a)")
    print()

    try:
        
        x = pollard_rho_dlog(p, a, b, r, max_iter=100000)
        print(f"Найденный x: {x}")

        
        if verify_dlog(p, a, b, x):
            print(f"Проверка пройдена: {a}^{x} ≡ {b} (mod {p})")
        else:
            print(f"Ошибка: {a}^{x} ≠ {b} (mod {p})")

    except ValueError as e:
        print(f"Ошибка: {e}")


    print()
    print("Проверка перебором (для демонстрации):")
    for test_x in range(r):
        if pow(a, test_x, p) == b:
            print(f"x = {test_x} {a}^{test_x} mod {p} = {pow(a, test_x, p)}")
            break





    
            






           


            





            



