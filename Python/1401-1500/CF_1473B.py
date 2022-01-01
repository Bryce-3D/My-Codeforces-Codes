t = int(input())

def gcd(a,b):
    while a != b:
        while b > a:
            b = b-a
        while a > b:
            a = a-b
    return a

def mult(s,c):
    prod = s
    for i in range(c-1):
        prod += s
    return prod

for i in range(t):
    a = input()
    b = input()
    l_a = len(a)
    l_b = len(b)

    d = gcd( l_a,l_b )
    d_a = l_a//d
    d_b = l_b//d

    x = mult(a,d_b)
    y = mult(b,d_a)

    if x == y:
        print(x)
    else:
        print(-1)
