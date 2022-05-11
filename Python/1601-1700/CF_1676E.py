#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Time complexity double check
1.) Sorting candies
    O(nlogn)
2.) Making cutoffs
    O(n)
3.) Performing q queries (linear search)
    O(nq)

But nq <= 10^4 * 1.5 * 10^5 = 1.5 * 10^9 too big

3.) Performing q queries (binary search)
    O(qlogn)

Now nq <= 2 * 10^6
Should be safe now
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    q = Kumi[1]
    candies = [int(i) for i in input().split()]
    candies.sort()

    #cutoffs[i] is the minimum weight for which at least 
    #i candies will be needed
    cutoffs = [0]
    for i in range(n):
        next_cutoff = cutoffs[-1] + candies[-i-1]
        cutoffs.append(next_cutoff)

    for Mado in range(q):
        query = int(input())

        #Binary search the position of query~~~~~~~~~~~~~~~~~~~~~~~~~
        if query <= 0:
            print(0)
        elif query > cutoffs[-1]:
            print(-1)
        else: #query must be possible and need at least 1 candy
            lower = 0
            upper = n
            while upper > lower:
                mid = (upper+lower)//2
                check = cutoffs[mid]
                if query <= check:
                    upper = mid
                else: #query > check
                    lower = mid+1
            print(upper)
