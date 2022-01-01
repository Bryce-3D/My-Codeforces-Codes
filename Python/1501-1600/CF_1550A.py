def ceilsqrt(n):
    k = int(n**0.5)
    if k**2 < n:
        while k**2 < n:
            k += 1
        return k
    else:
        while k**2 >= n:
            k -= 1
        return k+1

for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    print( ceilsqrt( int(input()) ) )
