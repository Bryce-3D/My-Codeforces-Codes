string = input()
l = len(string)

swap_space = [0]
for i in range(l-1):
    if string[i] != string[i+1]:
        swap_space.append(i+1)
swap_space.append(l)

swaps = len(swap_space)

check = 0
for i in range(swaps-1):
    if swap_space[i+1]-swap_space[i] >= 7:
        check += 1
        break

if check == 0:
    print('NO')
else:
    print('YES')
