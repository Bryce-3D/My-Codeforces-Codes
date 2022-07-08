#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Ideas
Probably O(n) (excluding possible sorting)
Turn the array of tasks into counts where count[i] is 
the number of tasks i specializes in.
Order of count doesn't actually matter, this can be sorted.

Two pointers going inward? Keep tossing from high end to low end somehow...

Use the count of the counts???


5 workers
tasks = [0,0,0,1,1,2,2,2,2,2,4]
counts = [3,2,5,0,1]
sorted counts = [0,1,2,3,5]
Relabel the workers so that sorted counts[i] 
is the number of tasks of worker i

Take these as the number of hours each worker has to work (currently all 
only work on their specialty)

hours[i] = number of workers that work i hours
hours = [1,1,1,0,1]
      = [0,1,2,0,0]   (toss fromworker with 5 hrs to worker with 0 hrs)

counts = [0,1,1,2,3,3,4,6,7,8,8,8]

hours = [1,2,1,2,1,0,1,1,3]
      = [0,2,2,2,1,0,1,2,2]
      = [0,0,2,4,1,0,1,4,0]
      = [0,0,0,4,3,0,3,2,0]
      = [0,0,0,2,3,2,5,0,0]
      = [0,0,0,0,3,4,3,0,0]
                     ^6 hrs is the ans? (ind = 6)



WAIT IDEA FROM CHECKING IF 6 IS THE ANS:
    Binary search the number of hours needed???

Use counts from earlier

Test if n hrs work:
    worker i has t >= n tasks -> Need to defer t-n tasks
    worker i has t < n tasks  -> Can take extra (n-t)//2 tasks
    check if deferred tasks <= extra tasks

'''

for Homu in range(int(input())):
    #Number of workers and tasks resp
    w,t = [int(i) for i in input().split()]
    tasks = [int(i)-1 for i in input().split()]   #0-indexed

    #count[i] returns the number of tasks worker i (0-ind) specializes in
    count = [0 for i in range(w)]
    for i in tasks:
        count[i] += 1

    #Perform the binary search
    #The answer is always in the interval (L,R]
    L = 0            #At least one task so 0 fails
    R = max(count)   #Letting everyone do their specialty yields max(count) hrs
    while R-L > 1:
        mid = (L+R)//2

        #Check if mid works
        deferred = 0   #Number of tasks that need to be deferred
        extra = 0      #Number of extra spots for deferred tasks
        for c in count:
            if c >= mid:
                deferred += c-mid     #Excess gets given away
            else:
                extra += (mid-c)//2   #Extra slots available (/2 since 2 hrs each)
        
        if deferred <= extra:   #If it works
            R = mid
        else:
            L = mid
    
    print(R)
