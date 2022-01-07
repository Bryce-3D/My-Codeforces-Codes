n = int(input())
l = [int(i) for i in input().split()]
n1 = l.count(1)
n2 = l.count(2)
n3 = n - n1 - n2
print(n - max(n1,n2,n3))
