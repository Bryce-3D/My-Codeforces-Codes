for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = int(input())
	Kumiko = input()

	#Number of frontal(?) 0s
	a = 0
	while a < n and Kumiko[a] == '0':
		a += 1

	#Number of trailing 1s
	b = 0
	while b < n and Kumiko[n-1-b] == '1':
		b += 1

	if a+b == n:
		print(Kumiko)
	else:
		front = '0' * (a+1)
		back = '1' * b
		print(front + back)
