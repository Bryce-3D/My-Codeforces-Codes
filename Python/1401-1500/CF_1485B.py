Walpurgisnatch = [ int(i) for i in input().split() ]
n = Walpurgisnatch[0]
cap = Walpurgisnatch[2]
master_list = [ int(i) for i in input().split() ]

for Mahou_Shoujo_Madoka_Magica in range( Walpurgisnatch[1] ):
    span = [ int(i)-1 for i in input().split() ]
    gaps = span[1]-span[0]

    #they differ not at the end
    ans = 2*( (master_list[span[1]]-master_list[span[0]]) - gaps )

    #they differ at the end
    ans += master_list[ span[0] ]-1
    ans += cap - master_list[ span[1] ]

    print(ans)
