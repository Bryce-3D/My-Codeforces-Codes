#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
The actual string doesn't matter, just the counts.

Since only 5 possible letters, maybe can bash and check for 
each letter the maximum length of an interesting story 
dominated by said letter.

Maybe like for each word, convert it to
    [a,b,c,d,e]
where
    a = count('a') - count('b','c','d','e')
and so on
*Can also just store [count('a'), ..., count('e')]
 then compute the differences later

Get all the a's, sort in reverse, then get the longest 
possible prefix with a positive sum.
Do similar for other letters.

Wait this shud actually work, worst step is O(nlogn) sort.
'''

for Homu in range(int(input())):
    n = int(input())

    #words[i] will return the list
    # [count('a'), count('b'), count('c'), count('d'), count('e'), length]
    words = []
    for i in range(n):
        word = input()
        next = []
        for i in range(5):
            c_i = chr(ord('a') + i)
            next.append(word.count(c_i))
        next.append(len(word))
        words.append(next)


    ans = 0
    
    #For each letter a,b,c,d,e
    for ind in range(5):
        #Dominance of char in a word is
        #   instances of char - instances of not-char
        char_dominance = []
        #Get the dominance of each word
        for i in range(n):
            next_dominance = 2 * words[i][ind] - words[i][5]
            char_dominance.append(next_dominance)
        #Sort the dominances in decreasing order
        char_dominance.sort()
        char_dominance.reverse()

        #Find the longest positive prefix
        max_len = 0
        next_sum = char_dominance[0]
        while max_len < n and next_sum > 0:
            max_len += 1
            if max_len < n:   #No more next_sum if at the end
                next_sum += char_dominance[max_len]
        #Update ans
        ans = max(ans, max_len)

    print(ans)
