n = int(input())
string = input()

A = 0
D = 0
for i in range(n):
    if string[i] == 'A':
        A += 1
    else:
        D += 1

if A > D:
    print('Anton')
elif A < D:
    print('Danik')
else:
    print('Friendship')
