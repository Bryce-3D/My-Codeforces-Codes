for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    n = int(input())
    heroes = [ int(i) for i in input().split() ]
    losers = heroes.count( min(heroes) )
    print(n-losers)
