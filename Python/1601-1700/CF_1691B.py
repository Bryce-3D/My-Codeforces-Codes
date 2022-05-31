#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
It can be shown by induction from the largest shoe size downwards 
that you must get the same shoe size after reshuffling.
Therefore possible iff each distinct size appears at least twice.

Alg:
1.) Linearly scan to find indices of adjacent neq values
2.) Check if these indices are all not consecutive
3.) If yes, bash out construction
4.) Else, print(-1)'''

for Homu in range(int(input())):
    n = int(input())
    sizes = [int(i) for i in input().split()]

    #Find places where shoe size jumps
    jumps = [-1]      #Mark the start
    for i in range(n-1):
        if sizes[i] != sizes[i+1]:
            jumps.append(i)
    jumps.append(n-1)   #Mark the end
    
    #Check if it's possible
    possible = True
    for i in range(len(jumps)-1):
        if jumps[i+1] - jumps[i] == 1:
            possible = False
            break
    
    if possible:
        ans = [0 for i in range(n)]   #Initialize the ans
        #For each interval
        for i in range(len(jumps)-1):
            L = jumps[i]+1
            R = jumps[i+1]
            ans[R] = L+1
            for i in range(L,R):
                ans[i] = i+2
        #Make it a string
        ans = [str(i) for i in ans]
        print(' '.join(ans))
    else:
        print(-1)
