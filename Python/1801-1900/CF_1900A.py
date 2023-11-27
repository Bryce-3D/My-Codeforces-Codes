#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Hole of size >= 3  -> Infinite water generator -> ans = 2
All holes < size 3 -> Cannot generate water, need to fill all manually
'''

for Homu in range(int(input())):
    n = int(input())
    s = input()

    a = []
    run = 0   #Length of streak of .'s
    for c in s:
        if c == '#' and run == 0:
            continue
        elif c == '#' and run != 0:
            a.append(run)
            run = 0
        else:
            run += 1
    if run != 0:
        a.append(run)
    
    ans = 0
    if len(a) != 0 and max(a) >= 3:
        ans = 2
    else:
        ans = sum(a)
    print(ans)
