#type 1 is A1, type 2 is R1C1
def type_check(cell_name):
    if cell_name[0] != 'R':
        return 1
    elif cell_name[1].isalpha():
        return 1
    elif 'C' not in cell_name:
        return 1
    else:
        return 2

    
#converts numbers to "excel letter base"
def num_to_let(num):
    num = int(num)
    let = ''
    length = 1

    #finding the length and subtracting shorter lengths
    while num > 26**length:
        num -= 26**length
        length += 1

    #converting the remaining number to letters
    num -= 1
    for i in range(length):
        let = chr( num%26 + ord('A') ) + let
        num = num//26
        
    return let

def convert(cell_name):
    n = len(cell_name)

    #A1 to R1C1
    if type_check(cell_name) == 1:
        #finding the division between letters and numbers
        d = 0
        check = 0
        while check == 0:
            if cell_name[d].isalpha():
                d += 1
            else:
                check = 1

        #getting the row number
        row = ''
        for i in range(d,n):
            row = row+cell_name[i]

        #getting the column number
        col = (26**d-26)//25
        for i in range(d):
            col += ( ord(cell_name[i]) - ord('A') )*26**(d-1-i)
        col += 1
        col = str(col)

        #putting it together
        return('R'+row+'C'+col)

    #R1C1 to A1
    else:
        #finding where C is
        C_place = 2
        while cell_name[C_place] != 'C':
            C_place += 1

        #getting the column number
        col = ''
        for i in range(C_place+1,n):
            col += cell_name[i]
        col = num_to_let(col)

        #getting the row number
        row = ''
        for i in range(1,C_place):
            row += cell_name[i]

        #putting it together
        return(col+row)
            
#doing the actual thing   
m = int(input())
for i in range(m):
    print( convert(input()) )
