l = input().split()
k = int(l[0])
n = int(l[1])
w = int(l[2])
borrow = k*w*(w+1)//2 -n

if borrow > 0:
    print(borrow)
else:
    print('0')
