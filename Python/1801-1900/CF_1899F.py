#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
After playing around on paper
Having a line graph kinda useful

LIGHTBULB MOMENT
Have a line of n-1 nodes and just constantly change the edge to the last one

Line of vertices 1 to n-1
If dist of d is desired, then connect vertex 0 to vertex d
'''

for Homu in range(int(input())):
    n,q = [int(i) for i in input().split()]

    #Line graph with n vertices
    for i in range(n-1):
        print(i+1,i+2)
    
    curr_d = 1

    for Kumi in range(q):
        next_d = int(input())

        if curr_d == next_d:
            print(-1,-1,-1)
        else:
            print(1,curr_d+1,next_d+1)   #Change from 0-ind to 1-ind
            curr_d = next_d
