Homura = input().split()
Madoka = set()
 
for i in range(3):
    Madoka.add(Homura[i])
 
print(list({'Alice', 'Bob', 'Cindy', 'Dani'} - Madoka)[0])
