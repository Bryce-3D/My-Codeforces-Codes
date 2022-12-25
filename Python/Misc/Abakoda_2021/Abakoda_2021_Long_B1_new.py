n = int(input())
dist = sorted([int(i) for i in input().split()])
skill = sorted([int(i) for i in input().split()])

possible = True
for i in range(n):
    if dist[i] > skill[i]:
        possible = False
        break

if possible:
    print('YES')
else:
    print('NO')
