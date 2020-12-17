f = open("input.txt", "r")

instruction = []
argument = []

for line in f:
	instruction.append(line.split()[0])
	argument.append(int(line.split()[1]))

acc = 0

def doInstructionsLoop():
	i = 0
	global acc
	acc = 0

	run = True

	l = []

	while i < len(instruction) and run:
		if instruction[i] == "acc":
			acc += argument[i]
			i += 1
		elif instruction[i] == "jmp":
			i += argument[i]
		elif instruction[i] == "nop":
			i += 1
		else:
			print(instruction[i])
			raise

		if i not in l:
			l.append(i)
		else:
			run = False
			return True

	return False


for j in range(len(instruction)):
	if instruction[j] == "jmp":
		instruction[j] = "nop"

		if not doInstructionsLoop():
			print(acc)

		instruction[j] = "jmp"
	elif instruction[j] == "nop":
		instruction[j] = "jmp"

		if not doInstructionsLoop():
			print(acc)
		
		instruction[j] = "nop"

	j += 1