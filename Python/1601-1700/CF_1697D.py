#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Do a linear trace

Do queries of the form 
    ? 2 1 i
for i = 2,3,...,n
*Take the query '? 2 1 0' to return 0
*'? 2 1 1' obviously will return 1

Two possibilities happen
    if '? 2 1 i' = '? 2 1 i-1':
        This means that there's a repeat.
        Need to trace back to the last instance of 
        each letter (STORE THIS) and compare with that 
        vs without that.
        This will let you determine the letter. 
        Record this as the newest latest instance of this letter
        Extra queries needed: At most 52
    if '? 2 1 i' = '? 2 1 i-1' + 1:
        New letter, just do the query
            '? 1 i'
        to determine the next letter.
        Record this as the latest appearance of said letter
        Extra queries needed: 1
Total number of queries is at most 5300 ish

WAIT NO IT"S 530000 FUCK

NEW IDEA:
When going left, you'll increase the variety by 1 each time 
you hit a prefix 
bsearch to find which letter
bsearch is approx 5, 5*1000 = 5000 which works now
'''

'''IMPORTANT
ALWAYS DO
    sys.stdout.flush()
AFTER EVERY PRINT
'''

#Number of distinct items in list from the Lth to Rth element
#NOT 0-INDEXED
def variety(list, L, R):
    ans = 0
    seen = set()
    for i in range(L-1,R):
        if list[i] not in seen:
            seen.add(list[i])
            ans += 1
    return ans





#Length of the ans
n = int(input())
#The answer
ans = []

#prefix_variety[i] returns the number of distinct letters
#Among the first i characters of the ans
prefix_variety = [0,1]

#last_seen[c] returns the index of the last occurence of c
#(NOT 0-indexed)
last_seen = {}

#last_seen_ind is the set of indices within last_seen
#last_seen_ind = {}


#Get the first charcter first
print('? 1 1')
sys.stdout.flush()
#Update the ans
ans.append(input())
#Update the last_seen
last_seen[ans[0]] = 1
#last_seen_ind.add(1)


#For every other character
for ind in range(2,n+1):
    #Check the next prefix_variety
    print(f'? 2 1 {ind}')
    sys.stdout.flush()
    prefix_variety.append(int(input()))

    #If a new character is discovered
    if prefix_variety[-1] != prefix_variety[-2]:
        #Check what the new character is
        print(f'? 1 {ind}')
        sys.stdout.flush()
        c = input()

        #Update the last_seen index for this character
        last_seen[c] = ind
        #last_seen_ind.add(ind)
        #Update the ans
        ans.append(c)

    
    #If the character is a repeat
    else:
        #Get the indices of last_seen and sort them
        l_i = [last_seen[c] for c in last_seen]
        l_i.sort()
        #Number of indices in l_i
        n_i = len(l_i)

        #Binary search
        L = 0
        R = n_i-1
        while L < R:
            mid = (L+R+1)//2
            #Check right half
            i_mid = l_i[mid]
            print(f'? 2 {i_mid} {ind}') #TODO
            sys.stdout.flush()
            c1 = int(input())

            #Compare to without ind
            c2 = variety(ans, i_mid, ind-1)

            if c1 > c2:   #character at ind is not in right half
                R = mid - 1
            else:   #character at ind is at right half
                L = mid
        
        #Now we'll have L=R and the next character is the one at index 
        #l_i[L]-1 of ans
        next = ans[ l_i[L] - 1 ]
        #Update ans, last_seen
        ans.append(next)
        last_seen[next] = ind


        '''
        for char in last_seen:   #For every character that has appeared so far
            i = last_seen[char]   #Index where char was last seen

            #Compare with i vs without i
            print(f'? 2 {i} {ind}')
            sys.stdout.flush()
            c1 = int(input())
            print(f'? 2 {i+1} {ind}')
            sys.stdout.flush()
            c2 = int(input())

            #Same count => character found
            if c1 == c2:
                #Update the last_seen
                last_seen[char] = ind
                #Update the ans
                ans.append(char)
                break
        '''
    

#Print the ans
str_ans = ''.join(ans)
print(f'! {str_ans}')
sys.stdout.flush()
