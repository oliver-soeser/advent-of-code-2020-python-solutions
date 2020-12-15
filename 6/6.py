f = open("input.txt", "r")

groups = [[]]
i = 0

for line in f:
	if line != "\n":
		for letter in line:
			groups[i].append(letter)
	else:
		groups.append([])
		i += 1



count = 0

for j in groups:
	nppl = j.count("\n")
	nyes = dict()
	for k in j:
		if k != "\n":
			nyes[k] = j.count(k)

	for l in nyes:
		print(l)
		if nyes[l] == nppl:
			count += 1


print(count)