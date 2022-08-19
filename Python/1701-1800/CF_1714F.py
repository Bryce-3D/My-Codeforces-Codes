#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
One of v1,v2,v3 must be in the path between the other two
Otherwise, we'd get a cycle

Therefore, 
    2 * max(d_12, d_23, d_31) = sum(d_12, d_23, d_31)

Afterwards, you just need to have 
    max(d_12, d_23, d_31) < n
Otherwise, you won't be able to fit enough vertices in between
*WAIT this is given as a constraint, so no need to check for this

If both are satisfied, just put enough vertices between stuff and 
do whatever for the remaining vertices

TEST 1 WA



Wait no
1 4
2 4
3 4
Gives the 3 distances are all 2 hold on

Compare path from 1 to 2 and path from 1 to 3
Suppose first k vertices (excluding 1 itself) are same in the path, then 
(k+1)-th one is diff
Then afterwards they can't have any common vertices (otherwise get a cycle)
Path from 2 to 3 would trace back along to that kth final common vertex then 
turn to the other one

    d_23 = (d_12-k) + (d_31-k)
    2k = d_12 + d_31 - d_23 = S - 2 * d_23

*Refer to that kth final common vertex as the center or something


Basically I need triangle inequality and will kinda make like the tangent 
segments formed from the incircle of a triangle

Need sum of d's be even and they satisfy triangle ineq

Get l1, l2, l3
Number of vertices used (including 1,2,3) is
    l1+l2+l3+1 = S//2 +1
(still holds when one of them is 0)



UPSOLVING ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Failed test case in test 2: 3 2 2 2
My result:
    YES
    1 4
    2 4
    3 4
Correct ans:
    NO

I'm not eliminating all wrong cases
Current:
    2*max > sum
    sum even

test case 9 8 8 8
segments are length 4,4,4
needs 4+4+4+1 = 13 vertices, too many

NEED EXTRA CHECK: Have enough vertices
gdi

Vertices needed = l1+l2+l3+1
'''

for Homu in range(int(input())):
    n, d_12, d_23, d_31 = [int(i) for i in input().split()]
    M = max(d_12, d_23, d_31)
    S = d_12 + d_23 + d_31

    l1 = S//2 - d_23   #Dist from v1 to center
    l2 = S//2 - d_31   #Dist from v2 to center
    l3 = S//2 - d_12   #Dist from v3 to center

    if 2*M > S or S%2 != 0 or l1+l2+l3+1 > n:
        print('NO')
    else:
        print('YES')

        if min(l1,l2,l3) == 0:   #If one of 1,2,3 is the center
            if l1 == 0:
                L, center, R = 3,1,2
                d_L, d_R = d_31, d_12
            elif l2 == 0:
                L, center, R = 1,2,3
                d_L, d_R = d_12, d_23
            else:
                L, center, R = 2,3,1
                d_L, d_R = d_23, d_31
            
            #L to center
            path_L = [L]
            for i in range(4, 3+d_L):
                path_L.append(i)
            path_L.append(center)
            for i in range(d_L):
                print(path_L[i], path_L[i+1])
            
            #R to center
            path_R = [R]
            for i in range(3+d_L, 2+d_L+d_R):
                path_R.append(i)
            path_R.append(center)
            for i in range(d_R):
                print(path_R[i], path_R[i+1])
        
        else:   #If none of 1,2,3 is the center
            #Designate 4 as the center

            #1 to 4
            path_1 = [1]
            for i in range(5, 4+l1):
                path_1.append(i)
            path_1.append(4)
            for i in range(l1):
                print(path_1[i], path_1[i+1])

            #2 to 4
            path_2 = [2]
            for i in range(4+l1, 3+l1+l2):
                path_2.append(i)
            path_2.append(4)
            for i in range(l2):
                print(path_2[i], path_2[i+1])

            #3 to 4
            path_3 = [3]
            for i in range(3+l1+l2, 2+l1+l2+l3):
                path_3.append(i)
            path_3.append(4)
            for i in range(l3):
                print(path_3[i], path_3[i+1]) 
        
        #Connect every remaining vertex to 1
        etc = [i for i in range(2+l1+l2+l3, n+1)]
        for v in etc:
            print(1,v)
