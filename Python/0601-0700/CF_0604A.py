#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

#Gets the score multiplied by 250 for problem p 
#with last time submission t and w WAs
def scaled_problem_score(p, t, w):
	max_pts = 500 * p
	abs_pts = (250 - t) * max_pts - 250 * 50 * w
	min_pts = 75 * max_pts
	return max(min_pts, abs_pts)

#Time of last submission
t = [int(i) for i in input().split()]
#Number of WAs
w = [int(i) for i in input().split()]
#Hack stats
h = [int(i) for i in input().split()]

#The total score
score = 0
#Points from solving problems
for i in range(5):
	score += scaled_problem_score(i+1, t[i], w[i])
score //= 250
#Points from hacks
score += 100 * h[0]
score -= 50 * h[1]

print(score)
