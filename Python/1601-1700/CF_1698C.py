#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
WLOG a is sorted in nondecreasing order

    a_1 <= a_2 < 0 < a_n-1 <= a_n
 -> a_3 > 0, a_n-2 < 0, contradiction

(1) Therefore, for n >= 5, there's at most 1 positive OR 
    at most 1 negative

    a_1 <= a_2 < 0
 -> a_1+a_2+a_3 < a_3
 -> a_1+a_2+a_3 = a_1 or a_2
 -> a_3 = -a_1 or -a_2
 -> a_3 > 0
 -> Everything else is positive
A similar argument holds when 0 < a_n-1 <= a_n

(2) Therefore, at least 2 negs -> rest positive
    At least 2 pos -> rest negative

(3) Therefore, 0 exists 
 -> at most 1 positive and at most 1 positive
 -> -a,0,...,0,a OR 0,...,0,a OR -a,0,...,0

Suppose that no 0 exists, then 
n = 3 -> sum of two of them is 0
n = 4 -> manually check
n >= 5 -> at most 1 pos or 1 neg by (1)
    Suppose at most 1 pos.
    Then at least 4 neg, so by (2), you have 2 
    negatives and rest are positive, contradiction!
    Similar for other case

Code Flow
if 0 in a:
    Check if it's of the forms
        -a,0,...,0,a OR 0,...,0,a OR -a,0,...,0
if 0 not in a:
    if n >= 5:
        no
    else:
        manually check
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    a.sort()

    if 0 in a:
        if a[1] != 0 or a[-2] != 0:
            print('nO')
        elif a[0] != 0 and a[-1] != 0 and a[0]+a[-1] != 0:
            print('nO')
        else:
            print('YeS')

    else: #0 not in a
        if n >= 5:
            print('nO')
        
        elif n == 3:
            if sum(a) in a:
                print('YeS')
            else:
                print('nO')

        else: #n == 4
            s = sum(a)
            if s-a[0] not in a:
                print('nO')
            elif s-a[1] not in a:
                print('nO')
            elif s-a[2] not in a:
                print('nO')
            elif s-a[3] not in a:
                print('nO')
            else:
                print('YeS')
