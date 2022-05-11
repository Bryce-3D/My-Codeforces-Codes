#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

def cost(w1, w2, l):
    ans = 0
    for i in range(l):
        c1 = w1[i]
        c2 = w2[i]
        v1 = ord(c1)
        v2 = ord(c2)
        ans += abs(v1-v2)
    return ans

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    l = Kumi[1]
    words = []
    for i in range(n):
        words.append(input())
    
    ans = cost(words[0], words[1], l)
    for i in range(n):
        for j in range(i+1,n):
            next_cost = cost(words[i], words[j], l)
            ans = min(ans, next_cost)
    
    print(ans)
