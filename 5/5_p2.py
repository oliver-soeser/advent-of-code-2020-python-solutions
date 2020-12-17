f = open("input.txt", "r")

passes = [[]]
i = 0

for line in f:
	for letter in line:
		if letter != "\n":
			passes[i].append(letter)
		else:
			passes.append([])
			i += 1

seats = []

for boardingpass in passes:
	rRange = [0, 127]
	cRange = [0, 7]
	for char in boardingpass:
		if char == "F":
			rRange[1] = rRange[0]+(rRange[1]+1-rRange[0])/2-1
		elif char == "B":
			rRange[0] = rRange[0]+(rRange[1]+1-rRange[0])/2
		elif char == "L":
			cRange[1] = cRange[0]+(cRange[1]+1-cRange[0])/2-1
		elif char == "R":
			cRange[0] = cRange[0]+(cRange[1]+1-cRange[0])/2
		else:
			raise

	if boardingpass != []:
		seatID = rRange[0]*8+cRange[0]
		seats.append(int(seatID))


seats.sort()

j = seats[0]+1

while j < seats[-1]:
	try:
		seats.index(j)
	except:
		print("Answer: ", j)

	j += 1