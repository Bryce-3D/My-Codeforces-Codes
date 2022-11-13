class Segtree:
    '''
    Initializes a segtree.
    (Uses `None` to pad it out to a perfect binary tree)

    Inputs:
        a   = Inputted array

        op  = operation to join segments
    '''

    #Fields
    _a = None      #Original array
    _n = None      #Length of a
    _op = None     #Join operator; modified to handle `None` inputs
    _seg = None    #Array to store the main segtree
    _span = None   #span[i] = interval [L:R] corresponding to seg[i]
    _l = None      #Length of seg

    def __init__(self, a, op):
        #Initialize other fields
        self.a = a
        self.n = len(a)
        #Modify `op` to handle `None` inputs
        def op_none(a,b):
            if a == None and b == None:
                return None
            elif a == None:
                return b
            elif b == None:
                return a
            else:
                return op(a,b)
        self.op = op_none

        #Calculate the length 
        k = 2 ** Segtree.ceil_log_2(self.n)   #Number of leaves (padded)
        self.l = 2*k - 1                      #Number of nodes

        #Initialize `seg`` with `None`s. Unused nodes will remain as `None`
        self.seg = [None for i in range(self.l)]
        #Initialize `span` with [n:n], the empty interval at the end
        self.span = [[self.n,self.n] for i in range(self.l)]

        #Initialize leaves of `seg` and `span`
        for i in range(self.n):
            #Copy `a` into the leaves of `seg`
            self.seg[i + k-1] = a[i]
            #Initilize `span` for the leaves
            self.span[i + k-1] = [i,i+1]
        
        #Initialize non-leaf nodes of `seg` and `span` bottom up
        for i in range(k-2,-1,-1):
            #Run the join operation to fill non-leaf nodes of `seg`
            self.seg[i] = self.op(self.seg[2*i+1], self.seg[2*i+2])
            #Join intervals of children to fill non-leaf nodes of `span`
            self.span[i] = [self.span[2*i+1][0], self.span[2*i+2][1]]



    '''
    Helper function for query.
    Returns the result of applying `op` on the interval `a[L:R]`
    Has an extra input `i` that represents the index of `seg` and `span` 
    currently being looked at to help traverse the segtree.
    [L:R] will always be contained entirely inside self.span[i].
    '''
    def help_me_query(self, L, R, i):
        #If [L:R] is exactly self.span[i], return the value in seg[i]
        L_0 = self.span[i][0]   #Left end of seg[i]'s interval
        R_0 = self.span[i][1]   #Right end of seg[i]'s interval
        if L == L_0 and R == R_0:
            return self.seg[i]
        
        #Check intervals of children of seg[i]
        l = self.span[2*i+1][0]     #Left end of left child
        m = self.span[2*i+1][1]     #Border of left and right child
        r = self.span[2*i+2][1]   #Right end of right child
        
        #If [L:R] is entirely in the left child of span[i]
        if R <= m:
            return self.help_me_query(L, R, 2*i+1)
        #If [L:R] is entirely in the right child of span[i]
        elif L >= m:
            return self.help_me_query(L, R, 2*i+2)
        #If [L:R] hits both the left and right child of span[i]
        else:
            #Ans of part of [L:R] in left subtree
            ans_L = self.help_me_query(L, m, 2*i+1)
            #Ans of part of [L:R] in right subtree
            ans_R = self.help_me_query(m, R, 2*i+2)
            #Join to get the ans
            return self.op(ans_L, ans_R)


    '''
    Returns the result of applying `op` on the interval `a[L:R]`
    '''
    def query(self, L, R):
        return self.help_me_query(L, R, 0)



    '''
    Updates `a[ind]` to `val` and updates `seg` accordingly
    '''
    def update(self, ind, val):
        k = self.l//2       #Number of non-leaf nodes
        i = k + ind         #Index of [ind:ind+1] in seg
        self.seg[i] = val   #Update seg[i]
        while i > 0:       #While not at the root
            #Go to the parent and update
            i = (i-1)//2
            self.seg[i] = self.op(self.seg[2*i+1], self.seg[2*i+2])
    
    '''
    Utility function to get the value of 
        ceil(log_2(n))
    Used to get the size of the array needed to store the segtree.
    '''
    @staticmethod
    def ceil_log_2(n):
        ans = 0
        exact = True   #True iff n is an exact power of 2

        #Iterate from LSB to MSB
        while n > 1:
            #If any bit except the MSB is 1, then not exact
            if n%2 == 1:
                exact = False
            #floor_log_2(n) = number of bits - 1
            ans += 1
            n >>= 1
        
        #Add an extra 1 if it is not exact
        if exact:
            return ans
        else:
            return ans+1


