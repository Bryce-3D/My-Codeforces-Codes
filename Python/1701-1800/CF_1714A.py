#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Return [hrs,mins] from H:M to h:m
def duration(H,M,h,m):
    hrs = h-H
    mins = m-M

    if mins < 0:
        hrs -= 1
        mins += 60
    if hrs < 0:
        hrs += 24
    
    return [hrs,mins]



for Homu in range(int(input())):
    n,H,M = [int(i) for i in input().split()]

    min_time = 24*60
    curr_ans = [24,0]

    for Kumi in range(n):
        h,m = [int(i) for i in input().split()]
        time = duration(H,M,h,m)

        if min_time > time[0]*60+time[1]:
            min_time = time[0]*60+time[1]
            curr_ans = time
    
    ans = ' '.join([str(i) for i in curr_ans])
    print(ans)
