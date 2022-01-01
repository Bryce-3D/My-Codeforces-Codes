def insert(a,b):
    a,b = min(a,b),max(a,b)
    b = (b+1)//2
    k = 0
    while a<b:
        k += 1
        a *= 2
    return k

for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    l = [ int(i) for i in input().split() ]
    ans = 0
    for i in range(n-1):
        ans += insert( l[i],l[i+1] )
    print(ans)
