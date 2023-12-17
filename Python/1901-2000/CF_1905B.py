#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Is it just ceil(k/2) where k = number of leaves?
'''

for Homu in range(int(input())):
    n = int(input())
    
    #deg[i] = degree of vertex i
    deg = [0 for i in range(n)]

    for Kumi in range(n-1):
        u,v = [int(i)-1 for i in input().split()]
        deg[u] += 1
        deg[v] += 1

    k = deg.count(1)
    ans = (k+1)//2
    print(ans)
