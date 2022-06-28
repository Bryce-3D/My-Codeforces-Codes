#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
2^15 approx 10^4, bsearch somehow

Trying small cases, kinda like pick the side with an "odd 
number of values within the correct half"???

YES CAUSE EACH ELEMENT EITHER
1.) Swap with outside -> WRONG now
2.) Swap with inside -> FORM A PAIR
So it's even EXCEPT FOR THE UNSWAPPED BOI WAIT YES
'''

#DON'T FORGET TO FLUSH
#    sys.stdout.flush()

for Homu in range(int(input())):
    n = int(input())

    #The ans must be in the range [L,R]
    L = 1
    R = n

    while R > L:
        mid = (R+L)//2

        #Query into the middle
        print(f'? {L} {mid}')
        sys.stdout.flush()

        #Check the number of values correctly in the interval [L,mid]
        response = [int(i) for i in input().split()]
        count = 0
        for i in response:
            if L <= i and i <= mid:
                count += 1
        
        #Check the parity to decide which side to recurse on
        if count%2 == 0:
            L = mid+1
        else:
            R = mid
    
    print(f'! {L}')
    sys.stdout.flush()
    

#DON'T FORGET TO FLUSH
#    sys.stdout.flush()
