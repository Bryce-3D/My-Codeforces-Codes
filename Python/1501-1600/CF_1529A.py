for Mahou_Shoujo_Madoka_Magica in range(int(input())):
    n = int(input())
    Soul_Gems = [ int(i) for i in input().split() ]
    print(n - Soul_Gems.count( min(Soul_Gems) ) )
