def extended_euclid(a, b):
    r0 = a 
    r1 = b
    x0 = 1
    k = 1
    x1 = 0 
    y0 = 0
    y1 = 1
    l = 1
    
    p = r1 // r0
    q = r1 % r0
    
    if q == 0:
        d = q
        x = x1
        y = y1
        return f"{a}*{x} + {b}*{y} = {d}"
    else: 
        x0 = x1
        y0 = y1
        r0 = r1
        r1 = q
        x1 = k - p * x1
        y1 = l - p * y1
        k = x0
        l = y0
        d = q

    return f"{a}*{y1} + {b}*{x1} = {d}"


def extended_euclid(a, b):
    num = a 
    num2 = b 
    x, xx, y, yy = 1, 0, 0, 1 

    while b:
        q = a // b 
        a, b = b, a % b 
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q

        return f"{x} * {num} + {y} * {num2} = {a}"
    

    def extended_binary_euclid(a, b):
        g = 1 
        while a % 2 == 0 and b % 2 == 0:
            a //= 2 
            b //= 2 
            g *= 2

        u = a 
        v = b 
        A = 1 
        B = 0 
        C = 0 
        D = 1

        while u != 0:
            if u % 2 == 0:
                u = u // 2
                if A % 2 == 0 and b % 2 == 0:
                    A //= 2 
                    B //= 2
                else: 
                    A = (A + B) // 2
                    B = (B - b) // 2

                if v % 2 == 0:
                    v //= 2
                    if C % 2 == 0 and D % 2 == 0:
                        C //= 2
                        D //= 2
                    else:
                        C = (C + b) // 2
                        D = (D - a) // 2

                if u >= v: 
                    u -= v
                    A -= C
                    B -= D
                else:
                    v -= u
                    C -= A
                    D -= B

            d = g * v
            x = C
            y = D 
            return (d, x, y)
        
        print("Перый алгоритм:")
        print(extended_euclid(6, 5))
        print("\первый алгоритм:")
        print(extended_euclid(6, 5))
        print("\nПервый алгоритм (бинарный):")
        print(extended_binary_euclid(6, 5))



