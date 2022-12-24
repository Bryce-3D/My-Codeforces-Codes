#link to prblems: https://codeforces.com/gym/102911
 
n = int(input())
k = n//4
 
if n%4 == 0:
    print('0')
    seq = ''
 
elif n%4 == 1:
    print('1')
    seq = 'A'
 
elif n%4 == 2:
    print('1')
    seq = 'AB'
 
elif n%4 == 3:
    print('0')
    seq = 'AAB'
 
for i in range(k):
    seq += 'BAAB'
 
print(seq)
