keyboard = ['qwertyuiop', 'asdfghjkl;', 'zxcvbnm,./']
l = len(keyboard[0])
r = len(keyboard)

shift = input()

#If a character `char` is in the dict `key[i]`, then key[i][char] returns
#the character that should've been pressed instead
if shift == 'L':
	key = [{keyboard[i][j] : keyboard[i][j+1] for j in range(l-1)} for i in range(r)]
elif shift == 'R':
	key = [{keyboard[i][j+1] : keyboard[i][j] for j in range(l-1)} for i in range(r)]

#corrector(char) returns the character that should've pressed instead of char
def corrector(char):
	for i in range(r):
		if char in key[i]:
			return key[i][char]

s_shift = input()
ans = ''
for i in range(len(s_shift)):
	ans += corrector(s_shift[i])
print(ans)
