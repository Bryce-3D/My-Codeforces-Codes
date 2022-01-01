for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	x = Homura[0]
	y = Homura[1]
	Madoka = [int(i) for i in input().split()]
	a = Madoka[0]
	b = Madoka[1]

	if 2 * a <= b:
		print(a * (x+y))
	else:
		print(b * min(x,y) + a * abs(x-y))
