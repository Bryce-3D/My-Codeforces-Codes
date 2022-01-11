#Idea
#Let the sequence be a,b,c
#AP is the same as a+c=2b
#Change each of a,b,c to satisfy said eq and check if it was scaled by an int

#For fast I/O
import sys
input = sys.stdin.readline

for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	l = [int(i) for i in input().split()]
	a = l[0]
	b = l[1]
	c = l[2]

	#Changing a
	new_a = 2*b-c
	m_a = new_a//a
	#Changing b
	new_b = (a+c)//2
	m_b = new_b//b
	#Changing c
	new_c = 2*b-a
	m_c = new_c//c

	if a*m_a == new_a and m_a > 0:
		print('YES')
	elif a+c == 2*new_b and b*m_b == new_b and m_b > 0:
		print('YES')
	elif c*m_c == new_c and m_c > 0:
		print('YES')
	else:
		print('NO')
