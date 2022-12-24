'''NOTE
This got 70/100 points
'''

yeet = [ int(i) for i in input().split() ]
n = yeet[0]
s = yeet[1]
boss = [ int(i) for i in input().split() ]
hp_up = [ int(i) for i in input().split() ]
 
hp = s
inv = []
win = True
for i in range(n):
    while hp < boss[i] and inv != []:
        use = inv.pop(0)
        hp += use
    if hp >= boss[i]:
        hp -= boss[i]
        inv.append( hp_up[i] )
        inv.sort(reverse = True)
    else:
        win = False
        end = i
        break
 
if win == True:
    print('WIN')
    print( n-len(inv) )
else:
    print('LOSE')
    print(i)
