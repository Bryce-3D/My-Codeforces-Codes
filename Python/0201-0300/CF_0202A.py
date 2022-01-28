#Main idea
#Note that if c is the lexicographically largest character of the string, then
#the answer is just spamming c as much as possible

#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

s = input()
c = max(s)
n = s.count(c)
print(c*n)
