f = open('input.txt', 'r')
l = f.read().split('\n')
f.close()

Homura = [int(i) for i in l[0].split()]
n = Homura[0]
k = Homura[1]-1
table = [int(i) for i in l[1].split()]

#Go clockwise until you find an available question
while table[k] == 0:
	k += 1
	k = k%n
k += 1
k = str(k)

f = open('output.txt', 'w')
f.write(k)
f.close()
