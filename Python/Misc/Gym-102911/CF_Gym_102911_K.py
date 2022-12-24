#link to prblems: https://codeforces.com/gym/102911
 
n = int(input())
power = [ int(i) for i in input().split() ]
maxed = max(power)
 
check = 1
for i in range(n):
    if maxed % power[i] != 0:
        check -= 1
        break
 
if check == 0:
    print(-1)
else:
    print( power.index(maxed) + 1 )
