for YEET in range( int(input()) ):
    seat_score = []
    for homura in range(6):
        seat_score.append( [ int(i) for i in input().split() ] )
    fren_space = []
    for homura in range(6):
        fren_space.append( [ int(i) for i in input().split() ] )
    fren_score = [ int(i) for i in input().split() ]
    whou_score = [ int(i) for i in input().split() ]

    hap_cap = -999999999999999999999999999999999999999999999999999999999999
    config = [0,1,2,3,4,5]

    #case runs over all permutations of [0,1,2,3,4,5]
    l = [0,1,2,3,4,5]
    
    for homura in range(6):
        l_homura = l.copy()
        e_homura = l_homura[homura]
        l_homura.remove( l_homura[homura] )
        
        for madoka in range(5):
            l_madoka = l_homura.copy()
            e_madoka = l_madoka[madoka]
            l_madoka.remove( l_madoka[madoka] )

            for mami in range(4):
                l_mami = l_madoka.copy()
                e_mami = l_mami[mami]
                l_mami.remove( l_mami[mami] )
                
                for kyoko in range(3):
                    l_kyoko = l_mami.copy()
                    e_kyoko = l_kyoko[kyoko]
                    l_kyoko.remove( l_kyoko[kyoko] )
                    
                    for sayaka in range(2):
                        l_sayaka = l_kyoko.copy()
                        e_sayaka = l_sayaka[sayaka]
                        l_sayaka.remove( l_sayaka[sayaka] )
                        e_kyubey = l_sayaka[0]

                        case=[e_homura,e_madoka,e_mami,e_kyoko,e_sayaka,e_kyubey]

                        happy = 0

                        #happiness from seats
                        for i in range(3):
                            happy += seat_score[case[i]][2-i]
                        for i in range(3):
                            happy += seat_score[case[i+3]][i]

                        #happiness from fren and whou
                        for i in range(6):
                            for j in range(i+1,6):
                                #if fren
                                if fren_space[case[i]][case[j]] == 1:
                                    if i<=2 and j>=3:
                                        happy += fren_score[j-i]
                                    else:
                                        happy += fren_score[j-i-1]
                                #if who u
                                else:
                                    if i<=2 and j>=3:
                                        happy -= whou_score[j-i]
                                    else:
                                        happy -= whou_score[j-i-1]

                        if happy > hap_cap:
                            hap_cap = happy
                            config = case

    left = str(config[0]+1)+str(config[1]+1)+str(config[2]+1)
    right = str(config[3]+1)+str(config[4]+1)+str(config[5]+1)
    config_formatted = left + '.' + right

    print(hap_cap)
    print(config_formatted)
