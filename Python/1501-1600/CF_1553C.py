for Mahou_Shoujo_Madoka_Magica in range( int(input()) ):
    while True:
        pred = input()
        A = [ pred[2*i] for i in range(5) ]
        B = [ pred[2*i+1] for i in range(5) ]
        a = [ A[i] for i in range(3) ].count('1')
        a_ = [ A[i] for i in range(3) ].count('?')
        b = [ B[i] for i in range(3) ].count('1')
        b_ = [ B[i] for i in range(3) ].count('?')

        if (a+a_)-b > 2 or (b+b_)-a > 2:
            print(6)
            break

        if A[3] == '1':
            a += 1
        elif A[3] == '?':
            a_ += 1

        if (a+a_)-b > 2 or (b+b_)-a > 1:
            print(7)
            break

        if B[3] == '1':
            b += 1
        elif B[3] == '?':
            b_ += 1

        if (a+a_)-b > 1 or (b+b_)-a > 1:
            print(8)
            break

        if A[4] == '1':
            a += 1
        elif A[4] == '?':
            a_ += 1

        if (a+a_)-b > 1 or (b+b_)-a > 0:
            print(9)
            break

        print(10)
        break
