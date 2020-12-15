f = open("input.txt", "r")

n = 0

for i in f:
    inp = i.split()
    pwd = inp[2]
    limits = inp[0].split("-")
    letter = inp[1][0]
    count = pwd.count(letter)

    if count >= int(limits[0]) and count <= int(limits[1]):
    	print("Valid!")
    	n += 1
    else:
    	print("Invalid")


print(n)