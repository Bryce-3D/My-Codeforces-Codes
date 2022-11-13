class Queue:
    '''
    Initializes a queue.
    Implemented by using 2 stacks.
    Enqueue places elements on top of stack 1.
    Dequeue takes elements from the top of stack 2.
    When an element is dequeued while stack 2 is empty, stack 1 is 
    emptied onto stack 2 in reverse order by popping each element 
    in stack 1 and pushing it into stack 2 until stack 1 is empty.
    '''

    #Fields
    _stack_1 = None   #Internal stack 1
    _stack_2 = None   #Internal stack 2
    _n       = None   #Number of elements currently in the queue

    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []
        self.n = 0
    
    '''
    Enqueues an element `k` at the back of the queue
    '''
    def enq(self, k):
        self.n += 1
        self.stack_1.append(k)
    
    '''
    Dequeues and returns the element at the front of the queue.
    If the queue is empty, it returns `None`.
    '''
    def deq(self):
        if self.n == 0:
            return None
        
        self.n -= 1
        #If stack 2 is empty
        if len(self.stack_2) == 0:
            #Transfer everything from stack 1 to stack 2
            while len(self.stack_1) != 0:
                next = self.stack_1.pop()
                self.stack_2.append(next)
        #Return the top of stack 2
        return self.stack_2.pop()
    
    '''
    Empties the queue
    '''
    def clear(self):
        self.stack_1 = []
        self.stack_2 = []
        self.n = 0
    
    '''
    Returns the current length of the queue
    '''
    def len(self):
        return self.n


