n = int( input() )
people = 0
cap = 0

for i in range(n):
    l = input().split()
    people -= int(l[0])
    people += int(l[1])
    if people > cap:
        cap = people

print(cap)
