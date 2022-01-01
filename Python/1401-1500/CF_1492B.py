for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    deck = [ int(i) for i in input().split() ]
    ans = [ [deck[0]] ]

    for i in range(1,n):
        if deck[i] > ans[-1][0]:
            ans += [ [deck[i]] ]
        else:
            ans[-1] += [ deck[i] ]

    l = len(ans)
    ans = [ ' '.join( str(i) for i in ans[l-1-j] ) for j in range(l) ]
    print( ' '.join(ans) )
