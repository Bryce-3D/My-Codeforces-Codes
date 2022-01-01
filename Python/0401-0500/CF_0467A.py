n = int(input())
yes = 0

for i in range(n):
    l = [ int(i) for i in input().split() ]
    if l[1] - l[0] >= 2:
        yes += 1

print(yes)
