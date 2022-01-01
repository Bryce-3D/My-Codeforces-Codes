for Mahou_Shoujo_Madoka_Magica in range(int(input())):
    a = input().split()
    b = input().split()
    a10 = int(a[1])
    b10 = int(b[1])
    l_a = len(a[0])
    l_b = len(b[0])

    if l_a + a10 > l_b + b10:
        print('>')
    elif l_a + a10 < l_b + b10:
        print('<')
    else:
        l = min(l_a,l_b)
        check = 0
        n_a = a[0]
        n_b = b[0]
        
        for i in range(l):
            if n_a[i] > n_b[i]:
                print('>')
                check = 1
                break
            elif n_a[i] < n_b[i]:
                print('<')
                check = 1
                break
            else:
                continue

        if check == 0:
            if n_a == n_b:
                print('=')
            elif l_a < l_b:
                b_0 = True
                for i in range(l_a,l_b):
                    if n_b[i] != '0':
                        b_0 = False
                        break
                if b_0:
                    print('=')
                else:
                    print('<')
            else:
                a_0 = True
                for i in range(l_b,l_a):
                    if n_a[i] != '0':
                        a_0 = False
                        break
                if a_0:
                    print('=')
                else:
                    print('>')
                
