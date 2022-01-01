def cycle(a,b):
    a += 1
    if a%b == 0:
        return b
    else:
        return a%b

for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    Homura = [ int(i) for i in input().split() ]
    #length of given and max of given numbers
    n = Homura[0]
    #number of colors
    k = Homura[1]
    #given numbers
    numbers = [ int(i) for i in input().split() ]
    #ith element stores indices where (i+1) appears
    indices = [ [] for i in range(n) ]

    for i in range(n):
        x = numbers[i]
        indices[x-1].append(i)

    #ith element states how many copies of (i+1) will be colored
    usable = [ min( k,len( indices[i] ) ) for i in range(n) ]
    #how many elements of the list will be colored
    to_use = ( sum(usable)//k )*k

    #the answer where I edit out the 0s
    coloring = [ 0 for i in range(n) ]

    #track which color I'm gonna add next, cycle using the cycle function
    color_tracker = 0
    #track how many have been colored so far so I don't overshoot
    used = 0
    #stop signal
    STOP = 0
    for i in range(n):
        for j in range( usable[i] ):
            used += 1
            color_tracker = cycle( color_tracker,k )
            coloring[ indices[i][j] ] = color_tracker

            if used == to_use:
                STOP = 1
                break
        if STOP == 1:
            break
                
    coloring = [ str(coloring[i]) for i in range(n) ]
    coloring = ' '.join(coloring)
    print(coloring)
