check = 0
row = 0
while check == 0:
    row += 1
    l = input().split()
    if '1' in l:
        check += 1
        col = l.index('1')+1

print( abs(row-3) + abs(col-3) )
