#Construction: [1, 2, 3, ..., n-k, n, n-k+1, n-1, n-k+2, n-2, ...]
#[1, 2, 3, ..., n-k-1] + [n-k, n, n-k+1, n-1, n-k+2, n-2, ...]

#ceil_div cause why not even tho I only need div by 2
#ceil_div(a.b) returns ceil(a/b)
def ceil_div(a,b):
	return (a-1) // b + 1 

#zigzag(x,y) returns the list [x, y-1, x+1, y-2, x+2, y-3, ...]
#which contains all the elements from x to y-1 exactly once
def zigzag(x,y):
	ans = [0 for i in range(y-x)]

	half_up = ceil_div(y-x,2)
	half_down = (y-x) // 2

	for i in range(half_up):
		ans[2*i] = x+i
	for i in range(half_down):
		ans[2*i+1] = y-1-i

	return ans

Homura = [int(i) for i in input().split()]
n = Homura[0]
k = Homura[1]

ans = [i for i in range(1, n-k)] + zigzag(n-k, n+1)
ans = [str(ans[i]) for i in range(n)]
print(' '.join(ans))
