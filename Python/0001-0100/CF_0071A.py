def abbrev(word):
    l = len(word)
    if l > 10:
        n = l-2
        return word[0] + str(n) + word[l-1]
    else:
        return word

for i in range( int( input() ) ):
    print( abbrev( input() ) )
