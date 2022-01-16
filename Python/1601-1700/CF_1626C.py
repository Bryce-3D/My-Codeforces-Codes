#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Ideas:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Scan from the right
#Check the maximum point at which the charging could've started while still
#successfully defeating the monster
#Continue scanning and decreasing the said "maximum charge starting point"
#if necessary until we reach the "maximum charge starting point" where it is
#its own "maximum charge starting point" (aka has hp 1)
#Once this happens, add it to a list of indices where the dmg will be reset
#and charged up again

#Realization: a monster doesn't exists at every second

#Instead calculate the "maximum charge starting point" for every monster
#Scan this list from right to left
#Take the rightmost element, check the corresponding element for any
#other monster within it's minimum charging frame
#If any of them have a lower "maximum charge starting point", change our
#current maximum charge starting point
#Also take note of that time this rightmost element is since we need the
#duration of the charge too
#Continue until all monsters in the interval we want to look at can be fully
#contained by the "maximum charge starting point"
#Take the length of this interval, toss it into a list of lengths of
#"charging intervals", and carry on

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Code Flow:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# - Store n, t (list of times), hp (list of hp's)
#   Have a scanner i that will go from right to left
#   Have a list of the lengths of "charging intervals" `charge_durations`
# - While i >= 0:
	# 1.) set `right_end` to be the right end of this interval
	# 2.) set `left_end` to be the "maximum charge starting point" of monster i
	# 3.) set `cycle_not_done` to True (set to False once we reach the state
	#   where all monsters in the interval are fully contained)
	# 4.) While cycle_not_done:
		# a.) subtract the scanner i by 1
		# x.) if i < 0, set cycle_not_done to False because we have gone
		#     through all the monsters
		# b.) if monster i appears before the left_end, set cycle_not_done
		#     to False because all monsters in said interval can work
		# c.) if monster i can fit in the interval (aka has a larger
		#     corresponding left_end), continue
		# d.) if monster i can't fit in the interval (aka has a strictly
		#     smaller left_end), update the left_end to be this left_end
		#     instead
	# 5.) Add the length of this interval to the list charge_durations
	# 6.) Turn each charge duration to its corresponding mana cost and
	#     add them all up

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = int(input())
	t = [int(i) for i in input().split()]
	hp = [int(i) for i in input().split()]

	i = n-1
	charge_durations = []

	while i >= 0:
		right_end = t[i]
		left_end = t[i] - hp[i] + 1
		cycle_not_done = True

		while cycle_not_done:
			i -= 1
			if i < 0:                            #No more remaining monsters
				cycle_not_done = False
			elif t[i] < left_end:                #All remaining monsters come before
				cycle_not_done = False
			elif t[i] - hp[i] + 1 >= left_end:   #This monster can fit in the interval
				continue
			else:                                #This monster cannot fit in the interval
				left_end = t[i] - hp[i] + 1

		charge_durations.append(right_end - left_end + 1)

	ans = 0
	for i in charge_durations:
		ans += i * (i+1) // 2
	print(ans)
