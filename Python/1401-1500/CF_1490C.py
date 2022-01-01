def icbrt(n):
	ans = int(n**(1/3))
	while ans**3 < n:
		ans += 1
	while ans**3 > n:
		ans -= 1
	return ans

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	x = int(input())
	b = icbrt(x)
	possible = False

	#b^3 cannot be exactly x since a and b must be nonzero
	if b**3 == x:
		b -= 1

	#WLOG a <= b and check b s.t. b^3 is in [x/2, x)
	while 2*b**3 >= x:
		a = icbrt(x - b**3)
		if a**3 + b**3 == x:
			possible = True
			break
		b -= 1

	if possible:
		print('Yes')
	else:
		print('nO')
