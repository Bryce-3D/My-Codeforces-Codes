#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Checks whether a string is a palindrome or not
def is_palindrome(s):
    L = 0
    R = len(s) - 1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

s = input()
l= len(s)
L = 0
R = l-1
insert = False   #Is it possible to do without an insert?

while L < R:
    if s[L] == s[R]:
        L += 1
        R -= 1
    else:
        insert = True
        break

#Can be done without an insert -> just insert in the middle
if not insert:
    mid = l//2
    ans = s[0:mid+1] + s[mid] + s[mid+1:l]
    print(ans)
#Cannot be done without an insert
#-> exists not equal symmetric pair
#-> must insert one of them
else:
    copy_L_char = s[0:R+1] + s[L] + s[R+1:l]   #Copy L char to the right
    copy_R_char = s[0:L] + s[R] + s[L:l]       #Copy R char to the left
    if is_palindrome(copy_L_char):
        print(copy_L_char)
    elif is_palindrome(copy_R_char):
        print(copy_R_char)
    else:
        print('NA')
