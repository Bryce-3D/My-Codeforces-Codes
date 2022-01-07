#For fast I/O
import sys
input = sys.stdin.readline

Homura = [int(i) for i in input().split()]
n = Homura[0]
p0 = Homura[1]
p1 = Homura[2]
p2 = Homura[3]
t0 = Homura[4]
t1 = Homura[5]

#break_power(t) returns the amount of watts used by Tom's laptop when left alone for
#t minutes after being used
def break_power(t):
	#Still normal mode
	if t <= t0:
		return t*p0
	#Reached screensaver
	elif t <= t0+t1:
		t -= t0
		return t0*p0 + t*p1
	#Reached sleep mode
	else:
		t -= t0+t1
		return t0*p0 + t1*p1 + t*p2


ans = 0 #The answer

#First interval to initialize `last_use`
interval = [int(i) for i in input().split()]
ans += (interval[1]-interval[0])*p0
last_use = interval[1] #The last time the laptop was used

#The other n-1 intervals
for i in range(n-1):
	interval = [int(i) for i in input().split()]
	break_time = interval[0] - last_use   #How long the laptop wasn't used
	work_time = interval[1] - interval[0] #How long the laptop was used
	ans += break_power(break_time)        #Power used during the break
	ans += work_time*p0                   #Power used during the current session
	last_use = interval[1]                #Update the last time the laptop was used

print(ans)
