yeet = input().split()
n = int(yeet[0])
t = int(yeet[1])
position = input()

for i in range(t):
    position = position.replace('BG','GB')

print(position)
