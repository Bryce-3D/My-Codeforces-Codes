#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

for Homu in range(int(input())):
    space = input()

    #board[r][c] returns the character at (r,c) (0-indexed)
    board = []
    for i in range(8):
        board.append(input())
    
    row_counts = []
    col_counts = []

    for r in range(8):
        row_counts.append(board[r].count('#'))
    
    for c in range(8):
        col_count = 0
        for r in range(8):
            if board[r][c] == '#':
                col_count += 1
        col_counts.append(col_count)

    row = 0
    col = 0
    
    for r in range(2,8):
        if row_counts[r-2] == 2 and row_counts[r] == 2 and row_counts[r-1] == 1:
            row = r
    for c in range(2,8):
        if col_counts[c-2] == 2 and col_counts[c] == 2 and col_counts[c-1] == 1:
            col = c
    
    print(row, col)
