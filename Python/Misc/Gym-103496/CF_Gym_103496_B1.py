n = int(input())
dist = [int(i) for i in input().split()]
skill = sorted([int(i) for i in input().split()])
 
possible = True
for i in range(n):
    if dist[i] > skill[i]:
        possible = False
 
if possible:
    print('YES')
else:
    print('NO')
