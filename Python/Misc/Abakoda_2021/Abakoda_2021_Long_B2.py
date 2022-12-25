#Number of people/spots
n = int(input())
#Distances of the spots from lowest to highest
dist = [int(i) for i in input().split()]
#People sorted from lowest to highest skill stat
skill = sorted([int(i) for i in input().split()])

#l_can[i] represents the number of spots that the ith person can handle
l_can = []
#trace dist as we go through the people from least to most skilled
tracer = 0
#Form l_can
for i in range(n):
	#If the tracer is still not at a larger element and is not at the end of dist, go to the next element of dist
	while tracer < n and dist[tracer] <= skill[i]:
		tracer += 1
	l_can.append(tracer)

#l_choices[i] represents the number of spots that the ith person can chose after the i people in front choose first
#This works because for any i,j with i<j, i can select spot s => j can select spot s
l_choices = []
for i in range(n):
	l_choices.append(max(l_can[i] - i, 0))

#Multiply to get the final answer
ans = 1
for i in range(n):
	ans *= l_choices[i]

print(ans)
