#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
#ith router connects to l[i-2]
l = [int(i) for i in input().split()]

path = [n]
while path[-1] != 1:
    path.append(l[path[-1]-2])

path = [str(i) for i in path[::-1]]
ans = ' '.join(path)
print(ans)
