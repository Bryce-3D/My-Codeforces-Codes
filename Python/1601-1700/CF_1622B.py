#Store the original ratings in the list `old_ratings`
#First find the number of disliked songs and liked songs
#Suppose there are `dislikes` disliked songs

#Scan through the list to find elements that are either
	#Disliked and originally rated > dislikes
	#Liked and originally rated <= dislikes
#For the 1st case, put the index and original score in lists `i_demote` and `score_big`
#For the 2nd case, put the index and original score in lists `i_promote` and `score_smol`

#Make a copy of old_ratings called `new_ratings`
#For i in i_demote, change new_ratings[i] to score_smol[i]
#For i in i_promote, change new_ratings[i] to score_big[i]

#Make each element of new_ratings into a string and print it

for Mahou_Shoujo_madoka_Magica in range(int(input())): 
	n = int(input())
	old_ratings = [int(i) for i in input().split()]
	data = input()
	dislikes = data.count('0')

	i_demote = []
	i_promote = []
	score_big = []
	score_smol = []

	for i in range(n):
		if old_ratings[i] > dislikes and data[i] == '0':
			i_demote.append(i)
			score_big.append(old_ratings[i])
		elif old_ratings[i] <= dislikes and data[i] == '1':
			i_promote.append(i)
			score_smol.append(old_ratings[i])

	new_ratings = old_ratings[::]

	l = len(i_demote)
	for i in range(l):
		new_ratings[i_demote[i]] = score_smol[i]
	for i in range(l):
		new_ratings[i_promote[i]] = score_big[i]

	new_ratings = [str(i) for i in new_ratings]
	print(' '.join(new_ratings))
