for Mahou_Shoujo_Madoka_Magica in range(int(input())):
	Madoka = input()
	Homura = [int(i) for i in input().split()]
	k = Homura[0]
	m = Homura[1]
	n = Homura[2]
	l_a = [int(i) for i in input().split()]
	l_b = [int(i) for i in input().split()]

	a = 0    #Current step of Monocarp
	b = 0    #Current step of Polycarp
	ans = [] #The valid set of steps, if it exists
	possible = True

	while a < m and b < n:
		if l_a[a] == 0:
			ans.append(0)
			a += 1
			k += 1
		elif l_a[a] <= k:
			ans.append(l_a[a])
			a += 1
		elif l_b[b] == 0:
			ans.append(0)
			b += 1
			k += 1
		elif l_b[b] <= k:
			ans.append(l_b[b])
			b += 1
		else:
			possible = False
			break

	if a == m and possible:
		while b < n:
			if l_b[b] == 0:
				ans.append(0)
				b += 1
				k += 1
			elif l_b[b] <= k:
				ans.append(l_b[b])
				b += 1
			else:
				possible = False
				break
	elif b == n and possible:
		while a < m:
			if l_a[a] == 0:
				ans.append(0)
				a += 1
				k += 1
			elif l_a[a] <= k:
				ans.append(l_a[a])
				a += 1
			else:
				possible = False
				break

	if possible:
		ans = [str(i) for i in ans]
		print(' '.join(ans))
	else:
		print(-1)
