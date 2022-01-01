n = input()
l_1 = len(n)

count = 0
for i in range(l_1):
    if n[i] == '4' or n[i] == '7':
        count += 1
count = str(count)
l_2 = len(count)

check = 0
for i in range(l_2):
    if count[i] == '4' or count[i] == '7':
        check += 1
        break

if check == 1:
    print('YES')
else:
    print('NO')
