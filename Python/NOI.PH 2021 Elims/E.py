#A is 65, Z is 90

def strord(string,l):
    val = 0
    for i in range(l):
        val += ( ord(string[i])-65 )*26**(l-1-i)
    return val

def ordstr(order,l):
    b26 = []
    while order >= 26:
        r = order%26
        b26.append(r)
        order = (order-r)//26
    b26.append(order)
    l_b26 = len(b26)
    
    let = ''
    for i in range( l - l_b26 ):
        let += 'A'
    for i in range( l_b26 ):
        let += chr( b26[l_b26-1-i]+65 )
    return let

homura = int(input())

for madoka in range(homura):
    string = input()
    length = len(string)
    l = 0
    
    while True:
        l += 1
        rin = {}
        rin = set()
        for i in range( length+1-l ):
            val = strord( string[ i:i+l ],l )
            rin.add( val )

        if len(rin) != 26**l:
            missing = 0
            while True:
                if missing in rin:
                    missing += 1
                else:
                    break
            ans = ordstr( missing,l )    
            break
        
    print(ans)
