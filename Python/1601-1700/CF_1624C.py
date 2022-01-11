#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#First spam //2 untill all elements are at most n
#Next maybe sort then whenever there are equal elements, //2 one of them
#Eventually we either have an element that is 0 (from 1//2) or terminate at a permutation
#Another idea: note that everything in (n/2, n] gets trimmed down to be <= n//2
#Therefore everything in (n/2,n] must already exist after the trim
#Aka everything from n//2+1 to n

#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	n = int(input())
	l = [int(i) for i in input().split()]

	possible = True

	while possible:
		#Trim out excess fat
		for i in range(n):
			while l[i] > n:
				l[i] //= 2

		#Exit at base case
		if n == 1:
			break

		#Check if n//2+1 to n exist and remove them
		for i in range(n//2+1,n+1):
			if i in l:
				l.remove(i)
			else:
				possible = False
				break

		n //= 2

	if possible:
		print('YES')
	else:
		print('NO')
