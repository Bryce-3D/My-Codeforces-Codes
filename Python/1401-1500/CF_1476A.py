#ceil_div(a,b) will return the value of ceil(a/b)
def ceil_div(a,b):
	return (a-1)//b + 1

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	n = Homura[0]
	k = Homura[1]

	#The sum should be the minimum multiple of k that is at least n
	total = k * ceil_div(n,k)
	print(ceil_div(total,n))
