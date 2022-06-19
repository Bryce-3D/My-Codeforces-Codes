#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
It is always optimal to open the first pipes due to how they overflow.

10^9 possible volumes, cannot precompute time for every possible volume.
Instead precompute time taken when first i pipes are opened for i = 1,..,n?
Then for each query binary search the time needed.

Suppose that we turn on the first i pipes.
Perform dp???
First i pipes open vs first i+1 pipes open.

Solve from scratch requires at least O(i) for first i pipes which cannot.
Therefore tere must be *some* sort of dp sol.

Maybe record the time it'll take for the ith faucet to reach the (i+1)-th 
compartment assuming the first i are all on?


Special thanks to Beacon for giving me hints.
Gdi I didn't realize you could indirectly calculate overflow, 
could've become CM at last if I did.
'''

n = int(input())
volumes = [int(i) for i in input().split()]

#Precompute time taken to fill it up if the first i are on for i=1,...,n ~~~~~~~~~~~~~~~~~~~~~~~~~~

#pre_sum[i] returns the sum of the first i tanks
pre_sum = [0]
for i in range(n):
    next = pre_sum[-1] + volumes[i]
    pre_sum.append(next)

#front_times[i] returns the amount of time needed to fill up the 
#first i+1 tanks assuming that the first i+1 faucets are all on
front_times = [volumes[0]]
for i in range(1,n):
    prev_time = front_times[-1]                    #Time needed for first i tanks
    prev_total_vol = pre_sum[i]                    #Total volume of first i tanks
    curr_vol = prev_time*(i+1) - prev_total_vol    #Total volume towards (i+1)th tank
    if curr_vol >= volumes[i]:                     #If flow towards (i+1)th tank is enough
        front_times.append(prev_time)              #Append the same time
    else:                                          #If flow towards (i+1)th tank is not enough
        req_vol = volumes[i] - curr_vol            #Remaining required volume
        extra_time = 1 + (req_vol-1)//(i+1)        #Time needed to fill the rest
        front_times.append(prev_time+extra_time)   #Append the incremented time

#time[i] returns the amount of time needed to fill up all the tanks 
#if the first i+1 faucets are turned on
time = []
for i in range(n):
    front_time = front_times[i]               #Time to fill up the first i+1 tanks
    curr_vol = front_time * (i+1)             #Total volume produced so far
    if curr_vol >= pre_sum[-1]:               #If current volume is enough to fill all
        time.append(front_time)               #Append the time
    else:                                     #If current volume is not enough to fill all
        req_vol = pre_sum[-1] - curr_vol      #Remaining required volume
        extra_time = 1 + (req_vol-1)//(i+1)   #Time needed to fill the rest
        time.append(front_time+extra_time)    #Append the incremented time



for Homu in range(int(input())):
    t = int(input())

    if time[-1] > t:   #If all pipes isn't fast enough
        print(-1)
    elif t >= time[0]:   #If 1 pipe is fast enough
        print(1)
    else:
        #Binary search index i such that time[i] > t >= time[i+1]
        L = 0
        R = n-1
        #The desired t will always be in the subarr time[L:R]
        while R-L > 1:
            mid = (L+R)//2
            if t < time[mid+1]:    #Too far left
                L = mid + 1
            elif time[mid] <= t:   #Too far right
                R = mid
            else:                  #Index found
                L = mid
                R = mid+1
        
        print(R+1)
