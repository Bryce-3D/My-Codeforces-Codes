#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Start from the endpoints
Need to color the front with something
Can greedily get the longest possible string that covers the front
Recurse forwards

Wait no
abcd   using   abc,cd
cannot delete the colored part

Wait this can be fixed by modifying it to 
    pick string that can go as far right as possible while *CONTAINING* 
    (not starting) at a certain characted

Given the small constraints this should be doable?

100 tests * 100 chars * 10 strs * 10 checks/(string*char) = 10^6
'''

for Homu in range(int(input())):
    text = input()
    l = len(text)

    n = int(input())
    strs = []
    for i in range(n):
        strs.append(input())
    

    #Stores the moves; each element is of the form [str_ind, start_ind]
    #where start_ind is the leftmost index where strs[str_ind] is used and 
    #str_ind and start_ind are both 0-indexed
    moves = []
    ind = 0           #Current index of leftmost non-red character in the text
    possible = True   #Flip to false if we hit an impossible part

    
    #while not stuck and not at the end
    while possible and ind < l:
        best_move = []   #The best possible move with at least 1 more red character
        best_inc = 0     #The number of new red chars from the best move
        
        #Check for each possible string
        for s_i in range(n):
            s = strs[s_i]
            l_s = len(s)


            #Bash all possible extentions using s until it works or out of options
            for i in range(l_s):
                start = ind - i   #Index to start using s on
                inc = l_s - i     #Number of new red chars if it works
                #If possible and longer than prev best
                if text[start:start+l_s] == s and inc > best_inc:
                    best_inc = inc
                    best_move = [s_i, start]
                    break
        
        if best_inc == 0:   #If nothing can extend
            possible = False
        else:               #If something can extend
            moves.append(best_move)
            ind += best_inc
    
    if possible:
        print(len(moves))
        for move in moves:
            print(move[0]+1, move[1]+1)
    else:
        print(-1)
