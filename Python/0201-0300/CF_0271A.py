n = input()

while True:
    n = int(n)
    n += 1
    n = str(n)
    l = len(n)
    if l > 4:
        n = 10234
        break
    elif n[0] not in [ n[i] for i in [1,2,3] ]:
        if n[1] not in [ n[i] for i in [2,3] ]:
            if n[2] != n[3]:
                break

print(n)
