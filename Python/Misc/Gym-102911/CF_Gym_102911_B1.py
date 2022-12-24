#link to prblems: https://codeforces.com/gym/102911
 
yeet = [ int(i) for i in input().split() ]
n = yeet[0]
k = yeet[1]
row = input().split()
 
count=[]
for i in range(k):
    count.append(0)
 
for i in range(n):
    plant = int(row[i])
    count[plant-1] += 1
 
ans = 1
for i in range(k):
    ans *= 2**count[i]-1
 
print(ans)
