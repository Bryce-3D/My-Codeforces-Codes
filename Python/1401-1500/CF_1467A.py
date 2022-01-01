t = int(input())

for z in range(t):
    n = int(input())
    if n >= 2:
        ans = '98'
        n -= 2
        for i in range( n//10 ):
            ans += '9012345678'
        for i in range( n%10 ):
            ans += str( (9+i)%10 )
        print(ans)
    else:
        print(9)
