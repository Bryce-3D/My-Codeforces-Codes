#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
If k <= n, then there is absolutely no benefit in visiting a 
spot more than once (already claimed bonus mushrooms from first 
visit and reduces bonus mushroom growth gained).

If k > n, then visit every spot at least once, and just keep 
going from end to end till time's up?
Ok so basically want last n moves to be a sweep from end to end 
(we want the last visit of each spot to be as late s possible)



Code flow
 - If k < n:
     - Get prefix sum array
     - Find maximal sum of a contiguous subarray of length k 
       by a linear sweep on prefix sum array
     - Add [0+1+...+(k-1)] = (k-1)(k)/2 to said sum
     - Return the ans
 - If k >= n:
     - Get sum of array (O(n))
     - Add [(k-1)+(k-2)+...+(k-n)] = nk - [n(n+1)/2] to said sum
     - Return the ans
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]
    a = [int(i) for i in input().split()]

    #Less moves than spots
    if k < n:
        #Prefix sum array
        a_prefix_sum = [0]
        for i in a:
            next = a_prefix_sum[-1] + i
            a_prefix_sum.append(next)

        #Array of sum of all contiguous subarrays of length k
        a_sum_k = []
        for i in range(n+1-k):
            next = a_prefix_sum[i+k] - a_prefix_sum[i]
            a_sum_k.append(next)
        #Max sum of a contiguous subarray of length k
        max_sum_k = max(a_sum_k)

        #Extra mushrooms from growth
        bonus = ((k-1)*k) // 2

        #Print the ans
        print(max_sum_k + bonus)
    
    #More moves than spots
    else:
        #Mushrooms from initial state
        initial = sum(a)

        #Extra mushrooms from growth
        bonus = n*k - (n*(n+1))//2

        #Print the ans
        print(initial + bonus)
