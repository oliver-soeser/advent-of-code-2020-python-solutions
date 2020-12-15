f = open("input.txt", "r")

groups = [[]]
i = 0

for line in f:
	if line != "\n":
		for letter in line:
			if letter != "\n":
				groups[i].append(letter)
	else:
		groups.append([])
		i += 1



count = 0

for j in groups:
	l1 = []
	for k in j:
		if k not in l1: 
			count += 1
			l1.append(k)

print(count)