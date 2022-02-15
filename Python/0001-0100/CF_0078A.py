#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Counts the number of vowels in a string
def count_vowels(s):
	a = s.count('a')
	e = s.count('e')
	i = s.count('i')
	o = s.count('o')
	u = s.count('u')
	return a+e+i+o+u

v1 = count_vowels(input())
v2 = count_vowels(input())
v3 = count_vowels(input())

if v1 == 5 and v2 == 7 and v3 == 5:
	print('YES')
else:
	print('NO')
