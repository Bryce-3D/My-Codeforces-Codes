#link to prblems: https://codeforces.com/gym/102911
 
n = int(input())
B = [ int(i) for i in input().split() ]
B.sort()
 
A = [ B[0] ]
for i in range(n-1):
    A.append(B[i+1]-B[i])
 
 
ans = ''
for i in range(n-1):
    ans += str(A[i])
    ans += ' '
ans += str(A[n-1])
 
print(ans)
