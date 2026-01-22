#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Note that n cannot be p_{i+2} in
    max(p_i, p_{i+1) > p_{i+2}
Therefore, n must be in the 1st 2 spots of the permutation.
If n is the 1st element, we will trivially pick it.
If n is the 2nd element, then 
 - Cannot pick both 1st and 2nd
 - Picking 2nd is better than 1st or none
Therefore, n must be picked in some optimal config.

Extending this idea
n-1 must either be in the 1st 2 spots or must have n within the 2 spots 
before it. Ignoring the corner case of n-1 in the 1st 2 spots.
    Case 1: n, n-1, _
        Obviously pick n-1
    Case 2: n, _, n-1
        Cannot pick both n-1 and _
        Picking n-1 is clearly better
Therefore, n-1 must be picked in some optimal config if it comes after n.
But what if n-1 is before n?
Only possible in
    n-1, n, ...
Then n-1 is not picked.

Pick max in any pair?
Claim: At least one number is picked for any 2 consecutive numbers in an 
optimal config?
Claim: The ff algo works:
    - Look at the 1st 2 terms
    - Pick the bigger between them
    - Delete the chosen number and any before it
    - Repeat until the list is exhausted
Proof:
    It suffices to show that there exists an optimal sol that selects the 
    biggest of the 1st 2 terms.
    But this basically boils down to the analysis that any optimal config 
    must pick n earlier.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

I'M STUPID I MISREAD THE QN we need sum
The above thing solves for longest dec subseq for the whole array
Need to sum over all subarrays.
The algo described above is quite "local" in the sense that each decision only 
involves numbers that are nearby, maybe we can abuse this fact.

Consider 3 consecutive numbers a,b,c in the (subarray).
When will we pick b?
    Case 1: b = max(a,b,c)
        Then whether the algo described above is looking at (a,b) or (b,c) 
        while scanning through the array, b will be picked.
    Case 2: b = min(a,b,c)
        Then whether the algo looks at (a,b) or (b,c), b will NOT be picked
    Case 3: b != max or min of a,b,c
        Then b is the middle, so either a>b>c or a<b<c
        a<b<c violates the problem constraints, so it must be a>b>c.
        Then if the algo 1st looks at b in (a,b) (selecting the item right 
        before a), then it'll pick a, then b, then continue on.
        If the algo 1st looks at b in (b,c) (selecting a in the prev step), 
        then it'll also pick b
        Therefore, b will always be picked in this case.
Therefore, b will be picked iff it is not smaller than both of its neighbors.
Suppose b is at index i (1 <= i <= n-2).
Then there are i*(n-1-i) subarrays including element b where b is not at the 
end of the subarray.
The formula works for i=0,n-1 too (0 subarrays), so it works for all indices.
Nice.

There is also the corner case of a number being at one of the ends.
Suppose the subarray length > 1
    Case 1: First number of subarray
        Picked iff > next number
    Case 2: Last number of subarray
        Not obvious :madocry:
        If prev > last, then obviously pick
        Suppose prev < last, then not so obvious.
        Suppose last 3 numbers are a,b,c with b<c.
        Case a: First look at c is (b,c)
            Then we pick c
        Case b: First look at c is (c)
            Then we pick c
        Oh good we pick c regardless, no corner case here.
        Always picked
Suppose the number is at index i.
Then there are 
    n-1-i subarrays where it is the first but not last
    i subarrays where it is the last but not the first

Finally there's the case of it being the only element, always picked.
'''

for Homu in range(int(input())):
    n = int(input())
    a = [int(i) for i in input().split()]
    ans = 0

    #Case 1: neither start nor end of subarray
    for i in range(1,n-1):
        if a[i] == min(a[i-1],a[i],a[i+1]):
            continue
        ans += i * (n-1-i)

    #Case 2: start or end of subarray of len > 1
    for i in range(n):
        #Start of subarray
        if i != n-1 and a[i] > a[i+1]:
            ans += n-1-i
        #End of subarray
        if i != 0:
            ans += i

    #Caes 3: subarray of len = 1
    ans += n

    print(ans)
