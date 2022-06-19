#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''NOTE
This got hacked shortly after the round and I have not yet gotten around to 
fixing it. Not sure what went wrong with the code. Hopefully will fix it soon.
'''


'''Idea
PART 1
Values can go up to 10^9 which is too big to initialize; use a hash
Make something like a dict indices where 
    i is in indices iff i is in the dice rolls (0-indexed)
    indices[i] returns a list of the indices where i appears
Now we can process for each possible guess of a number (which must be in 
indices, guessing an unrolled number if stupid)

PART 2
Now suppose that a number num appears at indices i_1,...,i_k
How to find the optimal range?
Maybe use something like two pointers???
Note that if [L:R] is optimal, then [L+1:R] must be better than [L+1:R+anything]

New Idea:
Check the increase in value (aka number of wins - number of losses) when 
extending from one end to another.
Now the max is the maximum sum of a (possibly empty) contiguous subarray of 
this + 1 (the starting point is a +1).
Maximum contiguous subarray sum sounds like a Googleable thing.
'''

#Given an array a, returns the list
#   [max_sum, L, R]
#where max_sum can be obtained from sum(a[L:R])
#If every term is negative, returns
#   [0,-1,-1]
def max_subarr(a):
    n = len(a)
    #corner case of empty array
    if n == 0:
        return [0,-1,-1]

    curr_max = [0,-1,-1]

    max_ending_here = [a[0], 0, 1]
    if a[0] > 0:
        curr_max = max_ending_here.copy()
    
    for ind in range(1,n):
        if max_ending_here[0] <= 0:   #If prev max <= 0 and won't help
            max_ending_here = [a[ind], ind, ind+1]
        else:   #If prev max > 0 and will help
            next_sum = max_ending_here[0] + a[ind]
            L = max_ending_here[1]
            max_ending_here = [next_sum, L, ind+1]
        
        #If the current max is better, update it
        if curr_max[0] < max_ending_here[0]:
            curr_max = max_ending_here.copy()
    
    return curr_max



for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]

    indices_of = {}
    for i in range(n):
        if a[i] not in indices_of:   #New element
            indices_of[a[i]] = [i]
        else:   #Existing element
            indices_of[a[i]].append(i)

    #Each element of best_per_guess if a list of the form
    #   [guess, best sum of this guess, left end, right end]
    best_per_guess = []
    
    for guess in indices_of:
        #Indices where the current guess appears
        indices = indices_of[guess]

        #DEBUG ~~~~~~~
        #print(indices)

        #jumps[i] returns the increase of correct-wrong guesses when the end is 
        #extended from indices[i] to indices[i+1]
        jumps = []
        for i in range(len(indices)-1):
            jumps.append(indices[i]-indices[i+1]+2)
        
        #DEBUG ~~~~~~~~
        #print(jumps)

        #Find the best subarray of jumps
        best_jumps = max_subarr(jumps)

        #DEBUG ~~~~~~~~~~
        #print(best_jumps)

        #If every jump is negative and bad
        if best_jumps[1] == -1:
            best_guess = [guess, 1, indices[0], indices[0]]
        #If there is a positive jump
        else:
            i_best_l = indices[best_jumps[1]]
            i_best_r = indices[best_jumps[2]]
            best_guess = [guess, best_jumps[0]+1, i_best_l, i_best_r]
        
        #Record the best for this guess
        best_per_guess.append(best_guess)
    
    #Retrieve the best solution
    best_sums = [i[1] for i in best_per_guess]
    best_sum = max(best_sums)

    for best_guess_ in best_per_guess:
        if best_guess_[1] == best_sum:
            print(best_guess_[0], best_guess_[2]+1, best_guess_[3]+1)
            break
    

    #DEBUG ~~~~~~~~~~~
    #print(best_per_guess)
