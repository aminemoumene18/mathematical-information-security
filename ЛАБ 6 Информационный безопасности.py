import math

def pollard_method(n, c):
    a = c
    b = c 
    d = 1
    f = lambda x: (x**2 + 5) % n
    while d == 1:
        a = f(a)
        b = f(f(b))
        d = math.gcd(abs(a - b), n)   
    if d==n:
        print(1)
        return "divisor not found"
    
    else:
        print(d)
        return d
    

    

pollard_method(1359331, 1)

def factors(n):
    k = round(math.sqrt(n))
    number_list = []
    for i in range(k, n+1):
        if n % i == 0:
            number_list.append(i)
            
    for j in number_list:
        print(f"{n} = {j}*{n//j}",end=",откуда ")
        res = (j + n//j) // 2 
        res_2 = int(math.sqrt(res**2 - n))
        print(f"s={res}, t={res_2} и {n}={res}² -{res_2}²")

factors(65)


    




    