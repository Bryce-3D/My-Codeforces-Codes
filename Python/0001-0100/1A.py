l = input().split()
n = int(l[0])
m = int(l[1])
a = int(l[2])

def ceildiv(a,b):
    return (a-1)//b+1

print(ceildiv(n,a)*ceildiv(m,a))
