#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
sum of n is <1000 so O(n^2) shud be fine
Greedily pick everything except the last two digits shud work I believe
The front elements are the most important even if the stuff behind 
becomes super suboptimal.
Yes can be shown it'll always exist
'''

for Homu in range(int(input())):
    n = int(input())
    p = [int(i) for i in input().split()]

    #Corner case
    if n == 1:
        print(-1)
    #n>1 will always have an ans
    else:
        used = set()
        ans = []
        
        for i in range(n-2):
            for j in range(1,n+1):
                if (p[i] != j) and (j not in used):
                    ans.append(j)
                    used.add(j)
                    break
        
        unused = []
        for i in range(1,n+1):
            if i not in used:
                unused.append(i)
        
        if unused[0] != p[-2] and unused[1] != p[-1]:
            ans.append(unused[0])
            ans.append(unused[1])
        else:
            ans.append(unused[1])
            ans.append(unused[0])

        ans = [str(i) for i in ans]
        ans = ' '.join(ans)
        print(ans)
