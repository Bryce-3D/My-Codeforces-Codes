#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]
    l = [int(i) for i in input().split()]
    l.sort()


    #Initialize list of values and their counts
    #using the first number of the `l`
    counts = {l[0]:1}
    values = [l[0]]
    #Scan through the rest of the list
    for i in range(1, n):
        next = l[i]
        if values[-1] != next:   #Not yet in values
            values.append(next)
            counts[next] = 1
        else:                    #Already in values
            counts[next] += 1
    

    #Initialize the search for the longest streak
    #using the first value in `values`
    curr = values[0]
    if counts[curr] >= k:
        curr_streak = [1, curr, curr]   #[length, L, R]
    else:
        curr_streak = [0, -1, -1]
    max_streak = [0, -1, -1]            #[length, L, R]


    #Scan through the other values
    for i in range(1,len(counts)):
        next = values[i]
        next_count = counts[next]

        #Currently not in a streak
        if curr_streak[0] == 0:
            #Next value starts a streak
            if next_count >= k:
                curr_streak = [1, next, next]
            #NOtherwise, no reset needed since streak already blank

        #Currently in an extendable streak
        elif next_count >= k and next-curr == 1:
            curr_streak[0] += 1
            curr_streak[2] += 1
        
        #Currently in a terminating streak
        else:
            #Check if current streak is better
            if curr_streak[0] > max_streak[0]:
                max_streak = curr_streak
            
            #Next value starts a streak
            if next_count >= k:
                curr_streak = [1, next, next]
            #Else reset curr streak
            else:
                curr_streak = [0, -1, -1]
        
        #Update the current value
        curr = next
    
    #Check in case it ended during an ongoing streak
    if curr_streak[0] > max_streak[0]:
        max_streak = curr_streak
    
    if max_streak[0] == 0:
        print(-1)
    else:
        print(max_streak[1], max_streak[2])
