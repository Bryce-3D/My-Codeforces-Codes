#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Just store the ff:
    sum of odds
    number of odds
    sum of evens
    number of evens
'''

for Homu in range(int(input())):
    n,q = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]

    n_odd = 0
    s_odd = 0
    n_even = 0
    s_even = 0
    for k in a:
        if k%2 == 0:
            n_even += 1
            s_even += k
        else:
            n_odd += 1
            s_odd += k
    
    for Kumi in range(q):
        type, x = [int(i) for i in input().split()]
        
        if type == 0:   #Add to evens
            s_even += n_even * x   #Increment sum
            if x%2 == 1:           #If parity is changed, update
                s_odd, s_even = s_odd+s_even, 0
                n_odd, n_even = n_odd+n_even, 0
        else:           #Add to odds
            s_odd += n_odd * x     #Increment sum
            if x%2 == 1:           #If parity is changed, update
                s_odd, s_even = 0, s_odd+s_even
                n_odd, n_even = 0, n_odd+n_even
    
        print(s_odd+s_even)
