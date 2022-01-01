for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    Homura = [ int(i) for i in input().split() ]
    Madoka = Homura.pop(0)
    wait = []
    for i in range(3):
        mod = Madoka%Homura[i]
        if mod == 0:
            wait.append(mod)
        else:
            wait.append(Homura[i]-mod)
    print( min(wait) )
