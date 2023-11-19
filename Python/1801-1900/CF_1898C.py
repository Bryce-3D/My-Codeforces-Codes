#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''IDEA
Maybe you can do some parity shenanigans

You must start at (0,0) and end at (R-1,C-1)
This will need at least R+C-2 moves to actually accomplish
Therefore
    K < R+C-2 -> Impossible

Color the grid in a checkerboard fashion
Let 
    (r,c) = red  for r+c even
          = blue for r+c odd
Therefore, we start from a red vertex and always alternate between 
a red and blue vertex kinda...
WLOG we always go on a red edge first.
Then we must always exit red vertices along red edges and always exit 
blue vertices along blue edges.

ALSO ANOTHER THING
K and R+C-2 must have the same parity
Because otherwise we'll always end on the vertex of the wrong color
Therefore
    K and R+C have different parity -> Impossible

Actually can't we just create a BRBR loop at the end and let the path cycle 
there until the quota is hit?
However, this is a +4 length each time, we need to have a +2
Simply do a
    _   _
     |_|
at the start to have a +2

Therefore it is always impossible as long as both dimensions are at least 3 
by the above construction (enough space to fit a loop at the end and the 
extra bump at the start)
     R B    (horizontal edges on row 0)
    R R R   (vertical edges between rows 0 and 1)
     B R
      B B
       R

What happens when at least one dimension is only 2?
Wait we are given R,C are both at least 3, how convenient


Let x denote any color
    P = red if R+C is even, blue otherwise
    Q = blue if R+C is even, red otherwise

Row 0  : RBRB...       (alternate the whole way)
Row 1  : Bxxx...xxxx
Row 2  : xxxx...xxxx
...
Row R-3: xxxx...xxxx
Row R-2: xxxx...xxxP
Row R-1: xxxx...xxxP

Col 0  : Rxxx...xxxx
Col 1  : Rxxx...xxxx
Col 2  : xxxx...xxxx
...
Col C-3: xxxx...xxxx
Col C-2: xxxx...xxxQ
Col C-1:     ...PQPQ   (alternate the whole way)

*For convenience just make every row aside from row 0 end in 0 for when R = 3,4
*Similarly make every col aside from col C-1 start with R for when C = 3,4

*Also for convenience make every row except row 0 start with B and every col 
except col C-1 end with Q


FUCK I FORMATTED IT WRONGLY

"Col 0"   : RRxx...xxx?
"Col 1"   : xxxx...xxx?
...
"Col C-3" : xxxx...xxxQ
"Col C-2" : xxxx...xxxP
"Col C-1" : xxxx...xxQQ
'''

for Homu in range(int(input())):
    #K = desired path length (number of edges)
    R,C,K = [int(i) for i in input().split()]

    #Cannot reach the end
    if K < R+C-2:
        print('nO')
        continue
    #Cannot end at the correct parity
    if (K-R-C)%2 != 0:
        print('nO')
        continue
    #Actually possible
    print('YeS')

    #How it will end depending on parity
    if (R+C)%2 == 0:
        P = 'R'
        Q = 'B'
    else:
        P = 'B'
        Q = 'R'

    #Print row 0
    r0 = ['B' for i in range(C-1)]
    for i in range(C-1):
        if i%2 == 0:
            r0[i] = 'R'
    r0 = ' '.join(r0)
    print(r0)

    #Print the other rows
    r = ['B' for i in range(C-1)]
    r[-1] = P
    r = ' '.join(r)
    for i in range(R-1):
        print(r)
    
    #Print col 0
    c0 = ['R' for i in range(C)]
    if C%2 == 0:
        c0[-1] = 'B'
    c0 = ' '.join(c0)
    print(c0)

    #Print the other cols
    c = [Q for i in range(C)]
    if R%2 == 0:
        c[-1] = P
    for i in range(R-2):
        c_s = ' '.join(c)
        print(c_s)
        #Alternate the last entry
        if c[-1] == P:
            c[-1] = Q
        else:
            c[-1] = P
    
    # #Print the other cols
    # c = ['R' for i in range(R-1)]
    # c[-1] = Q
    # c = ' '.join(c)
    # for i in range(C-1):
    #     print(c)
    
    # #Print col C-1
    # c0 = [Q for i in range(R-1)]
    # for i in range(1,R):
    #     if i%2 == 0:
    #         c0[-i] = P
    # c0 = ' '.join(c0)
    # print(c0)
