#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Idea
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is most definitely bsearch, 2^10 = 1024 = 1000+epsilon
#Idea: +n/2 and if floor(x/n) goes up, x is in the upper half aka (n/2,n), otherwise
#x is in (0,n/2)
#Keep narrowing it down until done
#Have an upper and lower limit tracker?

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Code Flow
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 1.) Take in inputs and initialize upper_limit of x, lower_limit of x, the value of
#     floor_div(x/n) (div), and the current total addition to x (delta)
# 2.) While upper_limit != lower_limit (aka range for x is not fully narrowed down),
#     check what is the range of x currently, inclusive of the additions so far (aka the
#     bounds + delta)
# 3.) Query a number k such that the range of values of the edited x will have a multiple
#     of n in the middle.
# 4.) Check if div increased of not. If div increased, then x must've been in the upper half
#     of the interval. Otherwise, it must've been in the lower half
# 5.) Update the bounds of x accordingly
# 6.) One upper_limit == lower_limit, print out any of them and win :D

#When we have (kn-r,kn+r) as our range, then it'll get cut into
#(kn-r,kn-1] and [kn,kn+r)
#If we get a range of the form [kn,kn+r]:
#range_x = r
#r//2 and r same mod n?
#only if r = r//2
#aka only if r=0 already
#Therefore no edge case of querying 0 here
#If we get a range of the form [kn-r,kn-1]:
#range_x = r-1
#(r-1)//2 and -1 same mod n?
#only if (r-1)//2 is n-1
#(r-1)//2 = n-1   =>   r-1 >= n-1   =>   r >= n
#no corner case here again

#For fast I/O and sys.stdout.flush()
import sys
input = sys.stdin.readline

n = int(input())
#upper_limit = n-1 #Upper bound for x based on queries
#lower_limit = 1   #Lower bound for x based on queries
upper_cur = n-1   #Upper bound for x including the added delta
lower_cur = 1     #Lower bound for x including the added delta
div = 0           #Current value of floor_div(x/n)
delta = 0         #How much has been added to x so far

while upper_cur != lower_cur:
	#Current length of the range
	range_x = upper_cur - lower_cur
	half_range = range_x//2

	#Query that we wish to perform
	#We wish to make it such that the upper value of the current x is range_x//2 mod n
	to_add = ( half_range - upper_cur ) % n
	#if range_x%2 == 0:
	#	to_add += 1

	upper_cur += to_add
	lower_cur += to_add
	delta += to_add

	#DEBUG
	#print(upper_cur)
	#print(lower_cur)

	print(f'+ {to_add}')
	sys.stdout.flush()

	new_div = int(input())

	#x is in the lower half
	if new_div == div:
		upper_cur = n * (div+1) - 1
	#x is in the upper half
	else:
		lower_cur = n * (div+1)
		div = new_div


print(f'! {lower_cur}')
sys.stdout.flush()
