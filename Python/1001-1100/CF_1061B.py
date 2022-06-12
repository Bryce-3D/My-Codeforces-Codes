#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
First of all, sort the columns, order doesn't matter

Trace up-right and count the number of blocks traversed?
If doesn't exist, either go right (right is same height and 
ur at the top) or go up (at the last column)
'''

n,h = [int(i) for i in input().split()]
heights = [int(i) for i in input().split()]

heights.sort()

total = sum(heights)

req = 1
x = 0
y = 1

#Trace till the last column
while x < n-1:
    #Go right
    x += 1
    #Go up if possible
    if heights[x] >= y+1:
        y += 1
    #Count the new block we're on
    req += 1

#Climb the last column
req += heights[-1] - y

print(total - req)
