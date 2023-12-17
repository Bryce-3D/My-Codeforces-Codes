#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Lexicographically largest substring must start from a copy of the 
lexicographically largest character in the string.
Due to substring < whole string lexicographically, it must always 
reach up till the end.
Therefore, each operation is essentially tossing the last character 
in front of one of the lexicographically largest characters

WAIT
SUBSEQUENCE, NOT SUBSTRING
Ok then it will first get all copies of whatever the largest character is.
But then what hmmm...

Wait it will still always include the last character
Hmmm

Lexicographically largest subsequence will always consist of a sequence of 
nonincreasing characters (if it increases at some point, such as 'xy', then 
tossing the smaller one in front to make it 'y' instead will always be better).
What this does is essentially rearranges this largest subsequence to become 
nondecreasing instead by reversing it.

CAN FIND LEXICOGRAPHICALLY LARGEST SUBSEQ USING A MONOTONIC STACK THING
Pop all smaller elements in front then push onto stack
Track indices along with it
After that can manually reverse the list then fix the string then check if 
it is sorted or not
If it is, then check how many non-max chars are in the largest subseq since 
they all need to move to the back
'''

for Homu in range(int(input())):
    n = int(input())
    a = [c for c in input()]

    #Find the max subsequence
    max_subseq = []
    for i in range(n):
        next = a[i]

        #Nuke max_subseq till empty to next is not larger
        while len(max_subseq) > 0 and next > max_subseq[-1][0]:
            max_subseq.pop()
        
        max_subseq.append([next,i])
    
    #Flip the string in a
    l = len(max_subseq)
    for i in range(l):
        c = max_subseq[i][0]
        ind = max_subseq[-i-1][1]
        a[ind] = c
    
    #Check if a is sorted
    possible = True
    for i in range(n-1):
        if a[i] > a[i+1]:
            possible = False
            break
    
    if not possible:
        print(-1)
        continue

    ans = len(max_subseq)
    max_char = max_subseq[0][0]
    i = 0
    while i < l:
        if max_subseq[i][0] != max_char:
            break
        ans -= 1
        i += 1
    
    print(ans)
