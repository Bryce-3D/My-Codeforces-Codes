#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Find the largest binary string that appears and convert it back to decimal

#Inputs
n = input()
l = len(n)

#Largest binary string that appears in list form
bin = [1 for i in range(l)]
for i in range(l):
    if int(n[i]) >= 2:
        break
    else:
        bin[i]= int(n[i])

#Converting the binary string to its numerical value
ans = 0
for i in range(l):
    ans += 2**(i) * bin[-i-1]

print(ans)
