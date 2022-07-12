#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    grid = [input() for i in range(n)]

    ans = 0
    k = n//2

    #For each quadrant
    for r in range(k):
        for c in range(k):
            n0 = 0

            if grid[r][c] == '0':
                n0 += 1
            if grid[c][n-1-r] == '0':
                n0 += 1
            if grid[n-1-r][n-1-c] == '0':
                n0 += 1
            if grid[n-1-c][r] == '0':
                n0 += 1
            
            ans += min(n0, 4-n0)

    #If n odd, check middle cross
    if n%2 == 1:
        for i in range(k):
            n0 = 0

            if grid[k][i] == '0':
                n0 += 1
            if grid[n-1-i][k] == '0':
                n0 += 1
            if grid[k][n-1-i] == '0':
                n0 += 1
            if grid[i][k] == '0':
                n0 += 1
            
            ans += min(n0, 4-n0)
    
    print(ans)
