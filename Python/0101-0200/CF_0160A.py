n = int(input())
coins_not_int = input().split()
coins_not_sorted = [int(x) for x in coins_not_int]
coins = sorted(coins_not_sorted, reverse = True)
total = sum(coins)

mine = 0
i = 0
while mine*2 <= total:
    mine += coins[i]
    i += 1

print(i)
