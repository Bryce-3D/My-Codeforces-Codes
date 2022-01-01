for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())//3
    l = [ int(i)%3 for i in input().split() ]
    a = l.count(0)-n
    b = l.count(1)-n
    l = [a,b,-a-b]
    m = l.index( max(l) )
    l = [ l[m], l[(m+1)%3], l[(m+2)%3] ]
    if l[2] <= 0:
        print(l[0]-l[2])
    else:
        print(2*l[2]+l[0])
