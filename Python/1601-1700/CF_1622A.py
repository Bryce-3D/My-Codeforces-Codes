for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	Homura = sorted(Homura)

	if Homura[2] == Homura[0] + Homura[1]:
		print('YES')
	elif Homura[0] == Homura[1] and Homura[2]%2 == 0:
		print('YES')
	elif Homura[1] == Homura[2] and Homura[0]%2 == 0:
		print('YES')
	else:
		print('NO')
