str_1 = input().lower()
str_2 = input().lower()
l = len(str_1)

i = 0
ans = 0
while ans == 0 and i<l:
    a = ord( str_1[i] )
    b = ord( str_2[i] )
    if a > b:
        ans += 1
    elif a < b:
        ans -= 1
    else:
        i += 1

print(ans)
