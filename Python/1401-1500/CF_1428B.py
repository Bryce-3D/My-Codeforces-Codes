for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    conveyors = input()

    if '<' in conveyors and '>' in conveyors:
        total = 0

        for i in range(n-1):
            if conveyors[i] == '-' or conveyors[i+1] == '-':
                total += 1
        
        if conveyors[0] == '-' or conveyors[n-1] == '-':
            total += 1

    else:
        total = n

    print(total)
