#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    s = int(input())

    if s <= 9:
        print(s)
    else:
        ans = [9]
        s -= 9

        while s >= ans[-1]:
            ans.append(ans[-1]-1)
            s -= ans[-1]
        
        ans.append(s)

        ans = ans[::-1]
        ans = [str(i) for i in ans]
        ans = ''.join(ans)
        print(ans)
