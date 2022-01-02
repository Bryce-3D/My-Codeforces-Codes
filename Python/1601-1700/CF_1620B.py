for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	w = Homura[0] #Length parallel to the x-axis
	h = Homura[1] #Length parallel to the y-axis

	x1 = [int(i) for i in input().split()]
	A_x1 = (x1[-1] - x1[1]) * h

	x2 = [int(i) for i in input().split()]
	A_x2 = (x2[-1] - x2[1]) * h

	y1 = [int(i) for i in input().split()]
	A_y1 = (y1[-1] - y1[1]) * w

	y2 = [int(i) for i in input().split()]
	A_y2 = (y2[-1] - y2[1]) * w

	print(max(A_x1,A_x2,A_y1,A_y2))
