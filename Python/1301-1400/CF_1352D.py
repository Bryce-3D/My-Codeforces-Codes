#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    n = int(input())
    candies = [int(i) for i in input().split()]

    prev_sum = candies[0]   #Sum of prev round
    L = 1                   #Alice's index at the left
    R = n-1                 #Bob's index at the right
    player = 2              #Current player, Alice = 1, Bob = 2
    playing = True          #Whether they are still playing
    A_total = candies[0]    #Total of Alice's eaten candies
    B_total = 0             #Total of Bob's eaten candies
    moves = 1               #Number of moves made

    #While they're still playing
    while playing:
        if L > R:   #Corner case of starting with 0 candies left
            playing = False
        elif player == 1:   #If Alice's turn
            moves += 1   #Increase move counter

            #Trace until no candies left or curr_sum is enough
            curr_sum = 0
            while L <= R and curr_sum <= prev_sum:
                curr_sum += candies[L]
                A_total += candies[L]
                L += 1
            
            if curr_sum > prev_sum:   #If there's still enough
                prev_sum = curr_sum   #Update prev_sum
                player = 2            #Swap players
            else:                     #If not enough left
                playing = False       #End
        
        else:   #If Bob's turn
            moves += 1   #Increase move counter

            #Trace until no candies left or curr_sum is enough
            curr_sum = 0
            while L <= R and curr_sum <= prev_sum:
                curr_sum += candies[R]
                B_total += candies[R]
                R -= 1

            if curr_sum > prev_sum:   #If there's still enough
                prev_sum = curr_sum   #Update prev_sum
                player = 1            #Swap players
            else:                     #If not enough left
                playing = False       #End
        
    print(moves, A_total, B_total)
