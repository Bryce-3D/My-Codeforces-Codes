#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Vasya will always buy at most 2 segments, the segment with the smallest left end
#and the segment with the largest right end. All other segments become irrelevant
#as the list of segments is gradually traversed. Therefore, only the segment with
#the lowest min and the highest max need to be stored as we take each input



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Code Flow for each test case
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.) Set min_seg and max_seg to be the first segment and print its price
# 2.) Set omni_seg to be the first segment and omni_on to True
# <Steps 2 to 5 will get looped n-1 times>
# 2.) Take in the new segment new_seg
# 3.) Compare new_seg's left with the min_seg's left
	# 3.1.) If smaller, replace min_seg with new_seg
	# 3.2.) If equal, change the price of min_seg to be the cheaper one
	# 3.3.) If larger, do nothing
# 4.) Compare new_seg's right with max_seg's right
	# 4.1.) If larger, replace max_seg with new_seg
	# 4.2.) If equal, change the price of max_seg to be the cheaper one
	# 4.3.) If smaller, do nothing
# 5.) Check for the existence of an omni_seg
	# 5.1.) If new_seg is an omni_seg
		# 5.1.1.) If omni_seg is still an omni_seg, get the cheaper one*
		# 5.1.2.) If not, set omni_seg to new_seg and omni_on to True
	# 5.2.) If new_seg is not an omni_seg 
		# 5.2.1.) If omni_seg is still an omni_seg, do nothing
		# 5.2.2.) If not, set omni_on to False

# 6.) Check whether min_seg and max_seg or omni_seg is better, if omni_seg exists

#*it can be shown that omni_on must've been set to True in this scenario
#min_seg and max_seg will contain the segment with the lowest left and highest right resp
#Step 3 checks if there is a lower or (equal and cheaper) segment unlocked
#Step 4 checks if there is a higher or (equal and cheaper) segment unlocked



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Actual Code
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Fast I/O for better speed
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	#s=1
	n = int(input())
	min_seg = [int(i) for i in input().split()]
	max_seg = [i for i in min_seg]
	omni_seg = [i for i in min_seg]
	omni_on = True
	print(min_seg[2])

	#s=2 to n
	for Koe_no_Katachi in range(n-1):
		#New segment that Vasya can purchase
		new_seg = [int(i) for i in input().split()]

		#Compare with min_seg
		if new_seg[0] < min_seg[0]:
			min_seg = [i for i in new_seg]
		elif new_seg[0] == min_seg[0]:
			min_seg[2] = min(min_seg[2],new_seg[2])

		#Compare with max_seg
		if new_seg[1] > max_seg[1]:
			max_seg = [i for i in new_seg]
		elif new_seg[1] == max_seg[1]:
			max_seg[2] = min(max_seg[2],new_seg[2])

		#Checking for the existence of an omni segment
		if new_seg[0] == min_seg[0] and new_seg[1] == max_seg[1]:
			omni_on = True
			if omni_seg[0] == min_seg[0] and omni_seg[1] == max_seg[1]:
				omni_seg[2] = min(omni_seg[2],new_seg[2])
			else:
				omni_seg = [i for i in new_seg]
		else:
			if omni_seg[0] == min_seg[0] and omni_seg[1] == max_seg[1]:
				omni_on = True
			else:
				omni_on = False


		if omni_on:
			print(min(min_seg[2]+max_seg[2],omni_seg[2]))
		else:
			print(min_seg[2]+max_seg[2])
