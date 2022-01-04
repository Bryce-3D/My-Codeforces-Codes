n = int(input())
members = input().split()
m = int(input())
present = input().split()

here = len( set(members).intersection(present) )

missing = n - here
why = m - here

print(here)
print(missing)
print(why)
