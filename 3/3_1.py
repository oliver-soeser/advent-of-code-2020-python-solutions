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

x = 0
y = 0

n = 0
errors = 0

while y < len(grid):
	try:
		if grid[y][x] == "#":
			n += 1

		x += 3
		y += 1

		if x >= len(grid[y]):
			x -= len(grid[y])
		elif x < 0:
			x += len(grid[y])
	except:
		y = len(grid)

print(n)