#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
Just greedy
log_2(10^9) \approx 30

wait I can't pick the same index repeatedly
n <= 2*10^5 allows for nlogn algs

Precompute 
    master = [v_2(i) for i in range(2*10^5)]
for each test case, get
    master[0:n]
then sort it and find the shortest prefix thats adds 
enough 2s for it to work (or possibly run out)
'''

#Given a positive integer n, returns floor(log_2(n))
def log_2(n):
    ans = 0
    while n > 1:
        ans += 1
        n >>= 1
    return ans

#Given a positive integer n, returns v_2(n)
def v_2(n):
    ans = 0
    while n%2 == 0:
        ans += 1
        n >>= 1
    return ans

#Precompute; master[i] = v_2(i)
master = [v_2(i) for i in range(1, 2 * 10**5 + 5)]


for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #Calculate the number of 2s required
    v_2s = [v_2(i) for i in a]
    s = sum(v_2s)
    req = n-s

    #Find the possible increments from an operation
    incrs = master[:n]
    incrs.sort()
    incrs = incrs[::-1]

    #Find least number to hit the req (if possible)
    ind = 0
    total = 0
    while total < req and ind < n:
        total += incrs[ind]
        ind += 1

    if total >= req:
        print(ind)
    else:
        print(-1)
