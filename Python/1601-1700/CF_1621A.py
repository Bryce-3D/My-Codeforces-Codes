for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	n = Homura[0]
	k = Homura[1]

	#At least 2k+1 rows/columns are needed
	if 2*k-1 <= n:
		empty_line = '.'*n

		#Lines 1 to 2k-2
		for i in range(k-1):
			line_i = '.'*(2*i) + 'R' + '.'*(n-2*i-1) #R at the (2i)-th place (0 indexed)
			print(line_i)
			print(empty_line)
		#Line 2k-1
		print('.'*(2*k-2) + 'R' + '.'*(n-2*k+1))
		#Remaining empty lines
		for i in range(n-2*k+1):
			print(empty_line)
	else:
		print(-1)
