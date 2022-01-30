#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

n = int(input())
cycles = n//4
r = n%4
end = {0:'', 1:'a', 2:'aa', 3:'aab'}

print('aabb'*cycles + end[r])
