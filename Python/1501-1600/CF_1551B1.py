#a is 97, z is 122

for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    string = input()
    usable = 0

    for i in range(97,123):
        usable += min( 2,string.count(chr(i)) )

    print( usable//2 )
