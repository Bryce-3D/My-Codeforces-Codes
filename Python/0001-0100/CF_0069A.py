n = int( input() )
x = 0
y = 0
z = 0

for i in range(n):
    l = input().split()
    x += int(l[0])
    y += int(l[1])
    z += int(l[2])

if x == 0 and y == 0 and z == 0:
    print('YES')
else:
    print('NO')
