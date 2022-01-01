string = input()
ans = string[0].upper()
l = len(string)

for i in range(1,l):
    ans += string[i]

print(ans)
