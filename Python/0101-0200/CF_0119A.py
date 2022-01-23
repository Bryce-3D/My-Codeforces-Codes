#gcd function
def gcd(a,b):
	if a < b:
		a,b = b,a
	while b != 0:
		a,b = b, a%b
	return a

#Inputs
Homura = [int(i) for i in input().split()]
a = Homura[0]
b = Homura[1]
n = Homura[2]
#Track whose turn it is
turn = 0

#Play the game
while n != 0:
	if turn == 0:
		n -= gcd(a,n)
		turn = 1
	else:
		n -= gcd(b,n)
		turn = 0

#The winner is the other person
print(1-turn)
