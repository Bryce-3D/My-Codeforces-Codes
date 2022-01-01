t = int(input())

for i in range(t):
    qwerty = [ int(i) for i in input().split() ]
    n = qwerty[0]
    d = qwerty[1]
    a = [ int(i) for i in input().split() ]

    if max(a) <= d:
        print('YES')
    else:
        smol1 = min(a)
        a.remove(smol1)
        smol2 = min(a)
        if smol1+smol2 <= d:
            print('YES')
        else:
            print('NO')
