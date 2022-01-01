l = [4,7,44,47,74,77,444,447,474,477,744,747,774,777]
n = int( input() )

check = 0
for i in range(14):
    if n%l[i] == 0:
        check += 1
        break

if check == 1:
    print('YES')
else:
    print('NO')
