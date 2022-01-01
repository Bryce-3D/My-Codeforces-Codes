for Mahou_Shoujo_Madoka_Magica in range(int(input())):
    n = int(input())
    l = [ int(i) for i in input().split() ]
    m = min(l)
    i = l.index(m)

    req = n//2
    count = 0
    k = 0
    while count < req:
        if k == i:
            k += 1
        else:
            print(str(l[k]) + ' ' + str(m))
            k += 1
            count += 1
