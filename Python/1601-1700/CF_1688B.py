#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Ideas
Fusion ->    even change by [-1,0,1]
Reduction -> even change by [-1,0]
Therefore once an odd exists, fuse it to the remaining evens till dead

Suppose all even
     v_2(a) = v_2(b)    ->   v_2(a+b) > v_2(a),v_2(b)        (made worse)
     v_2(a) != v_2(b)   ->   v_2(a+b) = min(v_2(a),v_2(b))   (no improvement)
Therefore fusion of evens is kinda(?) useless?

So
1.) Find term with least v_2
2.) Spam /2 it till odd
3.) Fuse it with all other evens
'''

#Returns the 2-addict-valuation of an integer n
def v_2(n):
    ans = 0
    while n%2 == 0:
        ans += 1
        n //= 2
    return ans

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    #Finding the minimum v_2 in a
    v_2s = [v_2(i) for i in a]
    min_v_2 = min(v_2s)

    #Finding the number of evens in a
    evens = 0
    for i in a:
        if i%2 == 0:
            evens += 1
    
    if min_v_2 == 0:   #Smash with odds right away
        print(evens)
    else:   #Reduce an even first
        print(min_v_2 + evens - 1)
