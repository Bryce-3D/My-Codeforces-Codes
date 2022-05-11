#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Returns the score of putting a bishop at (r,c) of a row x col board
def score(r,c,row,col,board):
    #Downhill diagonal~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    diag1 = 0
    #Determine the upper-leftmost square
    if r >= c:
        tracer_r = r-c
        tracer_c = 0
    else: #r < c
        tracer_r = 0
        tracer_c = c-r
    #Trace down the diagonal
    while tracer_r < row and tracer_c < col:
        diag1 += board[tracer_r][tracer_c]
        tracer_r += 1
        tracer_c += 1

    #Uphill diagonal~~~~~~~~~~~~~~~~~~~~~~~~~~~
    diag2 = 0
    #Determine the bottom-leftmost square
    if r+c < row:
        tracer_r = r+c
        tracer_c = 0
    else: #r+c >= row
        tracer_r = row-1
        tracer_c = r+c - (row-1)
    #Trace up the diagonal
    while tracer_r >= 0 and tracer_c < col:
        diag2 += board[tracer_r][tracer_c]
        tracer_r -= 1
        tracer_c += 1
    
    #Remove the double counted square (r,c)
    ans = diag1 + diag2 - board[r][c]
    return ans


for Homu in range(int(input())):
    Kumi = [int(i) for i in input().split()]
    row = Kumi[0]
    col = Kumi[1]

    #board[i][j] gives the value of the ith row and jth column
    board = []
    for i in range(row):
        board.append([int(i) for i in input().split()])
    
    #Manually check each cell, constraints allows for it
    ans = 0
    for i in range(row):
        for j in range(col):
            next_score = score(i,j,row,col,board)
            ans = max(ans, next_score)
    
    print(ans)
