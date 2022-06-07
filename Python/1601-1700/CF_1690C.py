#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
You can tell the duration of task i by looking at tasks i-1 and i
if end[i-1] <= start[i], then just
    duration = end[i] - start[i]
else:
    duration = end[i] - end[i-1]

Make more concise:
    duration = end[i] - max(end[i-1], start[i])
'''

for Homu in range(int(input())):
    n = int(input())
    start = [int(i) for i in input().split()]
    end = [int(i) for i in input().split()]

    #The first task is a corner case as no task came before
    duration = [end[0] - start[0]]

    for i in range(1,n):   #For every other task
        next = end[i] - max(end[i-1], start[i])
        duration.append(next)
    
    string_duration = [str(i) for i in duration]
    ans = ' '.join(string_duration)
    print(ans)
