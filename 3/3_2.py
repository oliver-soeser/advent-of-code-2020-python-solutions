f = open("input.txt", "r")

grid = [[]]
i = 0

for line in f:
	for letter in line:
		if letter != "\n":
			grid[i].append(letter)
		else:
			grid.append([])
			i += 1

def getNumberOfTrees(slopeX, slopeY):
	x = 0
	y = 0

	n = 0

	while y < len(grid):
		try:
			if grid[y][x] == "#":
				n += 1

			x += slopeX
			y += slopeY

			if x >= len(grid[y]):
				x -= len(grid[y])
			elif x < 0:
				x += len(grid[y])
		except:
			y = len(grid)

	return n

print(getNumberOfTrees(1, 1)*getNumberOfTrees(3, 1)*getNumberOfTrees(5, 1)*getNumberOfTrees(7, 1)*getNumberOfTrees(1, 2))