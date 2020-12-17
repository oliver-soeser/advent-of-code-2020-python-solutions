f = open("input.txt", "r")

instructions = []
units = []

posX = 0
posY = 0

rot = 0

for line in f:
	instructions.append(line[0])
	units.append(int(line[1:]))


for i in range(len(instructions)):
	print("-----------")
	print(instructions[i])
	print(units[i])
	print()
	print(posX)
	print(posY)
	print(rot)
	print()

	if instructions[i] == "N":
		posY -= units[i]
	elif instructions[i] == "S":
		posY += units[i]
	elif instructions[i] == "E":
		posX += units[i]
	elif instructions[i] == "W":
		posX -= units[i]
	elif instructions[i] == "L":
		rot += units[i]
	elif instructions[i] == "R":
		rot -= units[i]
	elif instructions[i] == "F":
		if rot == 0:
			posX += units[i]
		elif rot == 90:
			posY -= units[i]
		elif rot == 180:
			posX += units[i]
		elif rot == 270:
			posY += units[i]

	if rot >= 360:
		rot -= 360
	elif rot < 0:
		rot += 360

	print(posX)
	print(posY)
	print(rot)

print(posX)
print(posY)
print("Manhattan distance: ", abs(posX)+abs(posY))