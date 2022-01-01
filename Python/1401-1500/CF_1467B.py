def Int_check(a,b,c):
    if a<b and b>c:
        return 1
    elif a>b and b<c:
        return 1
    else:
        return 0
 
t = int(input())
 
for z in range(t):
    n = int(input())
    l = [ int(i) for i in input().split() ]
    if n >= 5:
 
        #Intimidation Counter
        Int = 0
        #Maximal Reduction Counter
        Red = 0
 
        #check 2nd spot
        b = Int_check(l[0],l[1],l[2])
        if b == 1:
            Int += 1
        Red = b + Int_check(l[1],l[2],l[3])
        
        #check 3rd to (n-2)th spot
        for i in range(2,n-2):
            b = Int_check(l[i-1],l[i],l[i+1])
            if b == 1:
                Int += 1
            if Red < 3:
                s=Int_check(l[i-2],l[i-1],l[i])+b+Int_check(l[i],l[i+1],l[i+2])
 
                x = Int_check(l[i-2],l[i-1],l[i+1])
                y = Int_check(l[i-1],l[i+1],l[i+2])
 
                Red = max( Red,s-x,s-y )
 
        #check (n-1)th spot
        b = Int_check(l[n-3],l[n-2],l[n-1])
        if b == 1:
            Int += 1
        Red = max( Red, b + Int_check(l[n-4],l[n-3],l[n-2]) )
 
        print(Int-Red)
 
    else:
        print(0)
