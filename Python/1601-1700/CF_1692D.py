#For fast I/O
import sys
input = lambda: sys.stdin.readline().strip()

'''Idea
1440 * 100 is small enough, brute force
Track seen times by storing in a set
'''

#Checks if a time is a palindrome
def isPalindrome(time):
    if time[0] != time[-1]:
        return False
    if time[1] != time[-2]:
        return False
    return True



for Homu in range(int(input())):
    Kumi = [i for i in input().split()]

    #time has the colon removed
    time = Kumi[0]
    time = time[0:2] + time[3:5]

    #Interval between checks
    x = int(Kumi[1])
    x_hrs = x//60
    x_mins = x%60

    seen = set()
    ans = 0

    for i in range(1440):
        #If not yet seen, check if it's a palindrome
        if time not in seen:
            #If it's a palindrome, add it to ans
            if isPalindrome(time):
                ans += 1
            #Record it as seen
            seen.add(time)

        #Go to the next time
        hrs = int(time[0:2])
        mins = int(time[2:4])

        hrs += x_hrs
        mins += x_mins
        if mins >= 60:
            hrs += 1
            mins -= 60
        if hrs >= 24:
            hrs -= 24

        #Convert next time back to a string
        if hrs < 10:
            hrs = '0' + str(hrs)
        else:
            hrs = str(hrs)
        if mins < 10:
            mins = '0' + str(mins)
        else:
            mins = str(mins)
        
        time = hrs + mins
    
    print(ans)
