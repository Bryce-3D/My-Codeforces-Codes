#link to prblems: https://codeforces.com/gym/102911
 
anime = [ int(i) for i in input().split() ]
n = anime[0]
k = anime[1]
 
if 2*k <= n:
    songs = input().split()
    shuffle = ''
    for i in range(k,n):
        shuffle += songs[i] + ' '
    for i in range(k):
        shuffle += songs[i] + ' '
 
    print('YES')
    print(shuffle)
else:
    print('NO')
