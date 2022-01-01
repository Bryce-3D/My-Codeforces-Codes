Homu = [ int(i) for i in input().split() ]
a = Homu[0]
x = Homu[1]
y = Homu[2]

if 0<x<a and 0<y<a:
    print(0)
elif x>a or y>a or x<0 or y<0:
    print(2)
else:
    print(1)
