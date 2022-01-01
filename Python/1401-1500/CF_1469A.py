def possible(string):
    if string[0] == ')':
        return 'no'
    elif string[-1] == '(':
        return 'no'
    elif len(string)%2 == 1:
        return 'no'
    else:
        return 'yes'

n = int( input() )
for i in range(n):
    print( possible(input()) )
