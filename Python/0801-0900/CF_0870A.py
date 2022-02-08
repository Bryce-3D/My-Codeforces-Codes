#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Answer given the 2 lists
def ans(l1,l2):
	#Common digit
	for i in range(1,10):
		if i in l1 and i in l2:
			return i

	#No common digit
	a = min(l1)
	b = min(l2)
	return 10 * min(a,b) + max(a,b)

#Homura = [int(i) for i in input().split()]
#m = Homura[0]
#n = Homura[1]
Mahou_Shoujo_Madoka_Magica = input()

l1 = [int(i) for i in input().split()]
l2 = [int(i) for i in input().split()]

print(ans(l1,l2))
