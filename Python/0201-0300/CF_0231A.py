total = 0

for i in range( int( input() ) ):
    l = input().split()
    s = int(l[0])+int(l[1])+int(l[2])
    if s >= 2:
        total += 1

print(total)
