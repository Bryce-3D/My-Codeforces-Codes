string = input().lower()
string = string.replace('a','')
string = string.replace('e','')
string = string.replace('i','')
string = string.replace('o','')
string = string.replace('u','')
string = string.replace('y','')

n = len(string)
ans = ''
for i in range(n):
    ans += '.'
    ans += string[i]

print(ans)
