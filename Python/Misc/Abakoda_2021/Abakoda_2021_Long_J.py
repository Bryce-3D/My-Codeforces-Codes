Homura = [int(i) for i in input().split()]
n = Homura[0]
t = Homura[1]
cards = input()

pts = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}

fixedSum = 0   #Sum of the non-joker cards
jokers = 0     #Number of joker cards
for i in range(n):
	if cards[i] == '*':
		jokers += 1
	else:
		fixedSum += pts[cards[i]]

req = t - fixedSum #Required sum from the joker cards

#Max and min possible sum of the joker cards
min_j = jokers
max_j = jokers * 10

if req >= min_j and req <= max_j:
	print('YES')

	#Do stuff to change the jokers to get the desired sum
	#Shift all cards down 1 point. This will also shift 'req' down by 'jokers' points
	#'req // 9' will be the number of 9+1='T' cards used
	#'req % 9' will determine the next joker's value, specifically '(req % 9) + 1'
	#The remaining cards will then all be set to 0+1='A' cards
	req = req - jokers   #Shift all cards 1 point down
	tens = req // 9      #Number of cardsthat will be set to 9+1=10
	rem = req % 9        #Remainder left after spamming 9+1=10 cards
	rem += 1             #Shift the card back up

	#Building up the cards with jokers replaced
	ans = ''
	c_tens = 0         #Number of jokers turned into 'T' cards so far
	rem_used = False   #Remembers if the remainder 'rem' has been assigned to a joker yet
	for i in range(n):
		#Copy the same card if it's not a joker
		if cards[i] != '*':
			ans += cards[i]
		#Have not yet used the desired number of 'T' cards
		elif c_tens < tens:
			c_tens += 1   #One more 'T' card used
			ans += 'T'    #Add a 'T' card to our 
		#Desired number of 'T' cards used but 'rem' hasn't been used yet
		elif not rem_used:
			rem_used = True   #'rem' ill be used here now
			if rem == 1:
				ans += 'A'
			else:
				ans += str(rem)
		#Spamming the remaining 'A' cards in
		else:
			ans += 'A'

	print(ans)

else:
	print('NO')
	
