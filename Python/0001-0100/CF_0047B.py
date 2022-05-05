#ord('A') is 65

#Given `X>Y`` or `Y<X``, returns 0,1,2 if X is A,B,C resp
def winner(descr):
    if descr[1] == '>':
        return ord(descr[0]) - 65
    else:
        return ord(descr[2]) - 65


inputs = [0,0,0]
for i in range(3):
    inputs[i] = input()

wins = [0,0,0]
for descr in inputs:
    wins[winner(descr)] += 1

if 2 not in wins:
    print('Impossible')
else:
    B = wins.index(0)
    S = wins.index(1)
    G = wins.index(2)
    ans = chr(B+65) + chr(S+65) + chr(G+65)
    print(ans)
