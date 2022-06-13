#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n,q = [int(i) for i in input().split()]
prices = [int(i) for i in input().split()]
prices.sort()

price_pref_sum = [0]
for i in range(n):
    next = price_pref_sum[-1] + prices[i]
    price_pref_sum.append(next)

for Homu in range(q):
    x,y = [int(i) for i in input().split()]
    print(price_pref_sum[-x-1+y] - price_pref_sum[-x-1])
