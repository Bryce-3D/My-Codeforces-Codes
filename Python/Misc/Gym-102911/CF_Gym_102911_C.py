'''NOTE
This got 70/100 points
'''

yeet = [ int(i) for i in input().split() ]
m = yeet[0]
n = yeet[1]
x = yeet[2]
y = yeet[3]
a = m-x
b = n-y
 
cap = max(m,n)
seive = [ i for i in range( 2,cap+1 ) ]
primes = []
 
while len(seive) != 0:
    p = seive[0]
    primes.append(p)
    k = seive[0]
    seive.remove(p)
    while k*p <= cap:
        if k*p in seive:
            seive.remove(k*p)
        k += 1
l = len(primes)
 
def count_prime(n):
    index = 0
    count = 0
    while index < l and primes[index] <= n:
        while n%primes[index] == 0:
            n //= primes[index]
            count += 1
        index += 1
    return count
 
i_count = []
for i in range(a,m+1):
    i_count.append( count_prime(i) )
    
j_count = []
for j in range(b,n+1):
    j_count.append( count_prime(j) )
 
ans = 0
for i in range(x+1):
    for j in range(y+1):
        if i_count[i] != j_count[j]:
            ans += 1
        
print(ans)
