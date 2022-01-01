# Z is 90, a is 97

s = input()
l = len(s)

low = 0
for i in range(l):
    if ord(s[i]) > 93:
        low += 1

if 2*low >= l:
    print( s.lower() )
else:
    print( s.upper() )
