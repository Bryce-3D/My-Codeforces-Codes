#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
Note that the operations are reversible.

Get the prefix sums of both arrays, divide them up 
into corresponding sections with equal sums?
Like the 4th sample case with
    3 9 | 6     | 3 | 12 12 36 12
    9 3 | 2 2 2 | 3 | 4 12 4 12 12 4 12 4 4

Split each array as much as possible and see if they're the same?
Feels intuitively correct...
Linearly scan, checking whether they have the same splits?


Change back to first idea, it shud work, just check that everything within 
corresponding sections are pairwise one is m^thing of other.
Can just take min amogthem 

Code flow:
l_a,l_b,a,b,m given


'''

#Checks whether a/b is a perfect power of m
'''
def perf_pow_ratio(a,b,m):
    #WLOG a >= b
    if a < b:
        a,b = b,a
    if a%b != 0:
        return False
    
    d = a//b
    exp = 1
    while exp < d:
        exp *= m
    return exp == d
'''

#Get "non-m" part
def div_spam(n,d):
    while n%d == 0:
        n //= d
    return n




for Homu in range(int(input())):
    l_a,m = [int(i) for i in input().split()]
    a = [int(i) for i in input().split()]
    l_b = int(input())
    b = [int(i) for i in input().split()]

    #pre_sum_a = sum(a[0:i])
    pre_sum_a = [0]
    for i in range(l_a):
        next = pre_sum_a[-1] + a[i]
        pre_sum_a.append(next)
    #pre_sum_b = sum(b[0:i])
    pre_sum_b = [0]
    for i in range(l_b):
        next = pre_sum_b[-1] + b[i]
        pre_sum_b.append(next)
    
    #First check if they have the same total sum
    if pre_sum_a[-1] != pre_sum_b[-1]:
        print('nO')
    
    #If they have the same total sum
    else:
        #Find subsections with the same sum
        i_a = 0
        i_b = 0
        #common_a[i] = x and common_b[i] = y implies that 
        #    sum(a[0:x]) = sum(b[0:y])
        common_a = []
        common_b = []

        #While not at the end yet
        while i_a <= l_a and i_b <= l_b:
            if pre_sum_a[i_a] == pre_sum_b[i_b]:   #If equal prefix sums
                common_a.append(i_a)
                common_b.append(i_b)
                i_a += 1
                i_b += 1
            elif pre_sum_a[i_a] > pre_sum_b[i_b]:   #Elif a bigger prefix sum
                i_b += 1
            else:                                   #Elif b bigger prefix sum
                i_a += 1
        

        #DEBUG
        #print(common_a)
        #print(common_b)

        
        possible = True
        
        #Check each contiguous block with the same sum
        for i in range(len(common_a)-1):
            subarr_a = a[common_a[i]:common_a[i+1]]   #Relevant subarray of a
            subarr_b = b[common_b[i]:common_b[i+1]]   #Relevant subarray of b

            #DEBUG
            #print(subarr_a)
            #print(subarr_b)

            #Check that they're all pairwise ratio is perfect power of m
            subarr_a = [div_spam(i,m) for i in subarr_a]
            subarr_b = [div_spam(i,m) for i in subarr_b]

            #DEBUG
            #print(subarr_a)
            #print(subarr_b)

            if max(subarr_a) != min(subarr_a) or max(subarr_b) != min(subarr_b) or max(subarr_a) != min(subarr_b):
                possible = False
                break
        
        if possible:
            print('YeS')
        else:
            print('nO')
