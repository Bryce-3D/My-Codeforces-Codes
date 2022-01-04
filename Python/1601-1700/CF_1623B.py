#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Whenever Alice mentions a range of length 1, then Bob must've picked the only number in
#that range when it was given. We can first print all of these out since the order does not
#matter. Afterwards, we can consider ranges of length 2. Consider [k,k+1]. No matter what
#Bob picked, the other number must've been already printed when we took care of the ranges
#of length 1. Therefore, if we store the chosen numbers that have been printed so far, we
#can just check which hasn't been printed yet. Same goes for when we next examine ranges of
#length 3. After the number has been picked and the range of length 3 has been split, the
#resulting ranges all have length strictly less than 3 and all those other numbers would've
#been printed by then. Also, distinct intervals of the same length cannot overlap due to 
#every pair of distinct intervals being either entirely disjoint or one being completely
#inside the other so scanning through the intervals of the same length in any order should
#be fine.

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Code flow for each test case
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.) Take in n and each interval Alice gave.
# 2.) Process and store the intervals Alice gave in a list of n lists called 'master_list'.
#     The ith list (0 indexed) of master_list will contain all the intervals of length i+1.
# 3.) Make a set `printed` containing all the numbers that Bob had chosen that have been
#     printed so far.
# 4.) For `intervals` in master_list: (`intervals` is all the intervals of a specific
#     length)
	# For `i` in intervals: (`i` is an interval given by Alive)
	# 4.1.) Scan through the i until the unique element not yet in printed is found.
	#       Call this element `chosen_one`
	# 4.2.) Add chosen_one to the set printed
	# 4.3.) Print i and chosen_one in one line


#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = int(input())                       #Original length of the interval
	master_list = [[] for i in range(n)]   #ith element contains intervals of length i+1

	#Add each of the n intervals to the corresponding list in master_list
	for i in range(n):
		Homura = [int(i) for i in input().split()]
		l = Homura[1] - Homura[0]
		master_list[l].append(Homura)

	printed = set()   #Set of numbers chosen by Bob that have already been printed

	for intervals in master_list:
		for i in intervals:
			chosen_one = i[0]   #Start the scan from the smallest element
			#Scan upwards until the unprinted number is found
			while chosen_one in printed:
				chosen_one += 1

			#Add chosen_one to printed since it's about to be printed
			printed.add(chosen_one)

			#Print the interval i and Bob's chosen number chosen_one
			to_print = [str(i[0]), str(i[1]), str(chosen_one)]
			print(' '.join(to_print))
