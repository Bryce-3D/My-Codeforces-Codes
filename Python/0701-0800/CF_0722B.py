n = int(input())
syllables = [ int(i) for i in input().split() ]

check = 0
for Homu in range(n):
    phrase = input()
    a = phrase.count('a')
    e = phrase.count('e')
    i = phrase.count('i')
    o = phrase.count('o')
    u = phrase.count('u')
    y = phrase.count('y')
    
    if a+e+i+o+u+y != syllables[Homu]:
        check += 21
        break

if check == 0:
    print('YES')
else:
    print('NO')
