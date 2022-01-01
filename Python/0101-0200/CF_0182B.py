d = int(input())
n = int(input())
days = [ int(i) for i in input().split() ]

overall = sum(days)-days[n-1]
ans = d*(n-1)-overall

print(ans)
