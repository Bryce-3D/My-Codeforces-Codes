from collections import deque as dq

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA

'''

N = 11

k = N//2
LO = 10**k
HI = int((10**N)**0.5) + 3

print(LO)
print(HI)

dig_counts = {}

for i in range(LO,HI):
    n = i*i
    s = str(n)
    digs = [c for c in s]
    digs.sort()
    digs = tuple(digs)
    if digs in dig_counts:
        dig_counts[digs] += 1
    else:
        dig_counts[digs] = 1

for digs in dig_counts:
    if dig_counts[digs] >= N:
        print(f'digits = {digs}, count = {dig_counts[digs]}')

# for Homu in range(int(input())):
#     n = int(input())
