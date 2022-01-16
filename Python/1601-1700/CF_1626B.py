#Idea:
#Ideally we want to choose 2 digits whose sum is at least 10 to maximize
#the number of digits

#Case 1: There are no pairs of adjacent digits that sum to at least 10
	#Case 1.1: The 2nd digit from the left is nonzero
		#Then combining the leading digits would increase the value of the
		#leading digit of the final result, which is optimal
	#Case 1.2: The 2nd digit from the left is 0
		#Combining the 2nd digit with either of its neighbors would increase
		#the value of the 2nd digit in the final result. Otherwise it would
		#not. Therefore this is ideal. (Also applies when we have more than
		#one 0 after the leading digit; it increases the leftmost
		#increase-able digit)
	#In conclusion: combine front 2 in either case here
#Case 2: There is a pair of adjacent digits that sum to 10
	#Then picking the adjacent pair ab in xxxabyyy would reduce the value by
	#9 * a000 where 000 and yyy have the same number of digits. Therefore, we
	#want to pick the rightmost instance to minimize the loss

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = input()
	l = len(n)
	no_sum_10 = True
	i = l-2

	while no_sum_10 and i >= 0:
		if int(n[i]) + int(n[i+1]) >= 10:
			no_sum_10 = False
			combination = str(int(n[i]) + int(n[i+1]))
		else:
			i -= 1
			

	if no_sum_10:
		combination = str(int(n[0]) + int(n[1]))
		print(combination + n[2:])
	else:
		print(n[0:i] + combination + n[i+2:])
