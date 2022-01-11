#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Due to the swapping, we can reorder them in any way we want. Therefore, the colored
#letters can be thought more of as a set rather than a list. Therefore, only the number
#of instances of each letter in the string s is relevant, so we can get that and disregard
#s afterwards. Call this list letter_count
#
#Next, we can toss in letters by pairs. We can get the number of instances of each letter
#and //2 it to get the number of pairs. Then we can get the number of leftovers by checking
#how many elements of letter_count are leftover that can be used as the central pivot of a
#palindromic string.
#
#Next we must divide the pairs evenly across all the k colors. pairs%k will get pairs//k+1
#while the rest will get pairs//k. Wait no we can just make them all have pairs//k pairs
#each, dumping the extra pairs doesn't help everyone aka the length of the min isn't
#affected anyway. This leaves the optimal number of solos to add a central pivot
#This also fixes the aforementioned corner case below
#
#Corner case?
#Something like aaaa and 3 colors
#If you assign pairs directly one of the colors becomes empty
#Wait no this case only happens when pairs < k in which pairs//k is 0 and it'd be 1 anyway
#Wait no it's still a corner case, because this has no solos so 0 remains the smallest one
#Essentially need to check if pairs >= k or not. If pairs < k, then the ans must be 1

#Note to self:
#ord('a') is 97, ord('z') is 122

#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Homura = [int(i) for i in input().split()]
	n = Homura[0]
	k = Homura[1]
	s = input()

	#letter_count[i] contains the number of instances of the ith letter in s
	letter_count = [s.count(chr(97+i)) for i in range(26)]

	#Number of pairs of same letters
	pairs = 0
	for i in range(26):
		pairs += letter_count[i]//2
	#Number of letters leftover without a pair
	solos = 0
	for i in range(26):
		if letter_count[i]%2 == 1:
			solos += 1

	#Number of pairs per color when distributed evenly
	pairs_each = pairs//k
	#Number of leftover pairs that will get converted to solos
	pairs_extra = pairs%k
	solos += pairs_extra*2

	#If there are enough solos, everything can be extended by 1
	if solos >= k:
		print(2*pairs_each+1)
	else:
		print(2*pairs_each)
