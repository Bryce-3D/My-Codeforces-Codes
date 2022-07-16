#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
View wrt 1s
Playign around:
    Contiguous blocks of 1 can't merge?
    Contiguous blocks of 1 can extend and retract both ways?
WAIT YES

Claim: number of blocks of 0s and number of blocks of 1s constant
Proof:
    Each operation never merges nor erases a block since middle element 
    changing doesn't connect/disconnect anything by condition

Possible iff:
    Same ends
and
    Same number of contiguous blocks of 1 (aka same number of pairs of 
    adjacent indices with diff entries, aka swap indices)

Min number of moves would be:
    Extend/retract each corresponding block of 1s till they align
    Any possible collision can be resolved by just changing the order of 
    moves to move the other thing out of the way first.
    Get sum of abs val of diff bet corresponding "swap indices"
'''

for Homu in range(int(input())):
    n = int(input())
    s1 = input()
    s2 = input()

    #A switch is an index i such that s[i] != s[i+1]
    s1_switches = []
    s2_switches = []
    for i in range(n-1):
        if s1[i] != s1[i+1]:
            s1_switches.append(i)
        if s2[i] != s2[i+1]:
            s2_switches.append(i)
    
    if s1[0] != s2[0] or s1[-1] != s2[-1]:
        print(-1)
    elif len(s1_switches) != len(s2_switches):
        print(-1)
    else:
        ans = 0
        for i in range(len(s1_switches)):
            ans += abs(s1_switches[i]-s2_switches[i])
        print(ans)
