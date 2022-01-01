pog = input().split()
n = int( pog[0] )
k = int( pog[1] )

for i in range(k):
    if n%10 == 0:
        n //= 10
    else:
        n -= 1

print(n)
