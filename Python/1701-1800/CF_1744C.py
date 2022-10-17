#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
c between a c and g like
    c ... c ... g
don't matter

Just linearly scan
'''

for Homu in range(int(input())):
    n,c = input().split()
    n = int(n)
    s = input()

    if c == 'g':
        print(0)
    else:
        ans = 0

        #To handle the case of needing to teleport back
        min_g = n+1
        max_c = -1

        streak = 0
        active = False   #True if a c was seen but not a g yet
        for i in range(n):
            #If currently looking for a g
            if active:
                streak += 1
                if s[i] == 'g':
                    ans = max(streak, ans)
                    streak = 0
                    active = False
            
            #If currently looking for a c
            else:
                if s[i] == c:
                    active = True
                    max_c = i
            
            #also update min_g/max_c
            if s[i] == 'g':
                min_g = min(i, min_g)
            #if s[i] == c and (not active):
            #    max_c = i
        
        #Corner case of teleporting around
        if active:
            tlp = (n+min_g) - max_c
            ans = max(tlp, ans)
        
        print(ans)
