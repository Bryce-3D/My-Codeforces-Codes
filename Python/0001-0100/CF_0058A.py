msg = input()
hi = 'hello'

try:
    pos = 0

    for i in range(5):
        check = 0
        while check == 0:
            if msg[pos] == hi[i]:
                check += 1
            pos += 1

    print('YES')

except:
    print('NO')
