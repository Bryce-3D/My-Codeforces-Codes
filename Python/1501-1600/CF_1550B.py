for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    asdf = [ int(i) for i in input().split() ]
    n = asdf[0]
    a = asdf[1]
    b = asdf[2]
    s = input()
    #a does not matter lmao just add the end

    if b >= 0:
        print( (a+b)*n )
        
    else:
        swaps = 0
        for i in range(n-1):
            if s[i] != s[i+1]:
                swaps += 1

        deletions = (swaps+3)//2
        print( a*n + deletions*b )
