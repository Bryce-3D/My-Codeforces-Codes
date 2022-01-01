for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    a = [ int(i) for i in input().split() ]
    ans = 0
    
    for i in range(n):
        #i and j here are 1 less than what the problem wants
        # so we want a_i to divide i+j+2 so j is -(i+2) mod a_i but how code
        # so j is from 0 to i-1
        #get approx i/a_i, at most ceil(i/a_i) satisfy the congruency
        s = (-(i+2))%a[i]
        for j in range( (i-1)//a[i] +1 ):
            if s+a[i]*j < i and a[i]*a[s+a[i]*j] == i+2 + s+a[i]*j:
                ans += 1

    print(ans)
