#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#PYTHON HAS BUILT IN SORT LMAOOOO
#Idea: Count by columns rather than rows
#Count the number of days a shop will be used while scanning through the list rather
#than scanning the entire list each day (or some other convoluted thing
for Homu in range(int(input())):
    #Getting the inputs
    Kumiko = [int(i) for i in input().split()]
    n = Kumiko[0]                                #Number of shops
    budget = Kumiko[1]                           #Budget per day
    costs = [int(i) for i in input().split()]    #Initial cost of each shop (unsorted)
    costs.sort()                                 #Now sorted
    
    cost_0 = 0   #Cost when buying up to this shop on day 1
    shgurr = 0   #Total number of sugar packs bought
    #Loop through each shop
    for i in range(n):
        cost_0 += costs[i]         #Add the current shop to day 1's cost
        excess = budget - cost_0   #Excess money when buying up to this shop on day 1
        if excess < 0:             #If it can't even be bought on day 1, don't use it
            break
        days = excess//(i+1) + 1   #Number of days where the current shop will be visited
        shgurr += days             #Add this shop to the total
    
    print(shgurr)
