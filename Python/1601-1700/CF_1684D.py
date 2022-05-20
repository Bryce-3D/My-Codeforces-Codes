#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''
Jumping over a trap when there are k traps left ahead has the same effect as
replacing the trap that was jumped over by a new trap that deals k damage.

Therefore, jumping over a trap with dmg d and k traps in front changes the 
total damage by
    k - d

Pick the jumps that are optimal until k jumps are picked OR until any further 
jump cannot decrease the total damage.

WAIT NO THE -1s ARE REMOVED WITH OTHER JUMPS IN THE FUTURE YABAI

FIX FIX FIX
The ith jump considered also removes an extra i-1 dmg due to removing the extra +1s.
Add this into consideration when jumping until dmg is not reduced.

WHen 0 indexed this becomes ith jump removes extra i dmg
'''

for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    n = Kumi[0]
    k = Kumi[1]
    traps = [int(i) for i in input().split()]

    #Initial total damage (no jumps)
    init_dmg = sum(traps)

    #Change in damage by a jump
    delta_dmg = [( (n-1-i) - traps[i] ) for i in range(n)]
    #Sort to get the best jump value
    delta_dmg.sort()

    #Factor in the bonus dmg reduction from jumps canceling each 
    #other's bonus dmg
    true_delta_dmg = [( delta_dmg[i] - i ) for i in range(n)]

    #Check the sum of the prefixes of true_delta_dmg up to length k
    prefix_sum_TDD = [0]
    for i in range(k):
        next_prefix_sum = prefix_sum_TDD[-1] + true_delta_dmg[i]
        prefix_sum_TDD.append(next_prefix_sum)
    
    #Check which prefix of TDD gives the best reduction
    best_dmg_red = min(prefix_sum_TDD)

    #Minimum possible dmg taken
    min_dmg = init_dmg + best_dmg_red
    print(min_dmg)
