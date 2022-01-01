l = int (input() )
string = input()

swaps = 0
for i in range(l-1):
    if string[i] != string[i+1]:
        swaps += 1

print(l-1-swaps)
