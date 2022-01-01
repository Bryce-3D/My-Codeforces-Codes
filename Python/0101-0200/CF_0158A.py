yeet = input().split()
n = int(yeet[0])
k = int(yeet[1])
l = input().split()

cutoff = k

if int(l[k-1]) > 0:
    while cutoff <= n-1 and int(l[cutoff]) == int(l[k-1]):
        cutoff += 1
else:
    while cutoff >= 1 and int(l[cutoff-1]) <= 0:
        cutoff -= 1

print(cutoff)
