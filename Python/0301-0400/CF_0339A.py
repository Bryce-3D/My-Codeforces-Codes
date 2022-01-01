l = input().split('+')
n = len(l)
ones = 0
twos = 0
threes = 0

for i in range(n):
    if l[i] == '1':
        ones += 1
    elif l[i] == '2':
        twos += 1
    else:
        threes += 1

ans = ''
for i in range(ones):
    ans += '+1'
for i in range(twos):
    ans += '+2'
for i in range(threes):
    ans += '+3'
ans = ans.replace('+','',1)

print(ans)
