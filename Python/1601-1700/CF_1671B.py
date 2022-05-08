#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Main idea: 3 possible starts, afterwards everything is fixed
#Therefore you can just check each of the 3 possibilities
#This is 3*O(n) which is still O(n)
for Homu in range(int(input())):
    n = int(input())
    coords = [int(i) for i in input().split()]
    possible = False

    #Check for each possible shift of the start
    for shift in range(-1,2):
        #Check if it's possible with the current shift from the start
        start = coords[0] + shift
        possible_case = True
        for i in range(n):
            if abs(coords[i] - start - i) > 1:
                possible_case = False
                break
        #Update possible, and if it works, we're done
        possible = possible_case
        if possible:
            break

    if possible:
        print('YES')
    else:
        print('NO')
