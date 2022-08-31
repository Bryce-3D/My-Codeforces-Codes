#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

s = input()
seen = set()
n = 0

for c in s:
    if c not in seen:
        seen.add(c)
        n += 1

if n%2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
