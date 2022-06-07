#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Basically spamming permutations means having some cycles that shift 
by 1 at every iteration.
The main issue is that the items being shifted are not necessarily distinct.
How to check when a cycle repeats?

IDEA: The number of divisors of n is < 2sqrt(n)
Therefore can linearly check which characters are the same as the first one
Then for each of these (at most n), check if the index divides n.
If yes, then manually check if it cycles (O(n) each)
Therefore this is O(n*sqrt(n)) (very loose bound since d(n) < 2sqrt(n) is super 
loose for large n.


Code flow:

Have a set `checked` of checked indices
Have a list `min_cycles`

for i in range(n):
    if i not in `checked`:
        Cycle through the permutation to find the cycle starting at i
        Add cycled indices to `checked`
        Get the characters traversed in this cycle.
        for each character same as the start
            If same and index is div by length of cycle (aka cycle is feasible):
                verify manually if the cycle works
                if works, get the min shift (index)
                append this to `min_cycles`
                break loop

Get lcm of `min_cycles`
(implement Euclid alg, use ab = gcd(a,b)lcm(a,b), do it by pairs)
'''

#Returns gcd(a,b) where a,b >= 0 and at least one of a,b is nonzero
def gcd(a,b):
    if a < b:
        a,b = b,a
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


#Returns lcm(a,b) where a,b > 0
def lcm(a,b):
    return a * b // gcd(a,b)


#Main code
for Homu in range(int(input())):
    n = int(input())
    s = input()
    p = [int(i)-1 for i in input().split()]   #0-indexed

    checked = set()
    min_cycles = []


    #Find the min cycle length for all cycles
    for i_0 in range(n):
        if i_0 not in checked:
            #Get the cycle starting at i
            cycle = [i_0]
            tracer = p[i_0]
            while tracer != i_0:
                cycle.append(tracer)
                tracer = p[tracer]
            
            #Add everything from the cycle to `checked`
            for i in cycle:
                checked.add(i)
            
            #Get the characters traversed in this cycle
            chars = [s[i] for i in cycle]


            #Find min cycle length of chars
            l = len(chars)
            shortcut = False   #If there is a shorter cycle than the trivial one of length l
            for ind in range(1,l//2 + 1):   #For each character in the first half(except the first)
                if chars[ind] == chars[0] and l%ind == 0:   #If cycle is possible
                    #Manually verify if the cycle indeed works
                    works = True
                    for i in range(l):
                        c1 = chars[i]
                        c2 = chars[(i+ind)%l]
                        if c1 != c2:
                            works = False
                            break
                    #If it works, record the length and break
                    if works:
                        shortcut = True
                        min_cycles.append(ind)
                        break
            #If no shorter cycles exist
            if not shortcut:
                min_cycles.append(l)
    

    #Get the lcm of all elements of min_cycles
    ans = min_cycles[0]
    for i in range(1, len(min_cycles)):
        next = min_cycles[i]
        ans = lcm(ans, next)
    
    print(ans)
