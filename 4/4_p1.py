f = open("input.txt", "r")
passports = [{}]
i = 0

for line in f:
	if line != "\n":
		for item in line.split():
			passports[i][item.split(":")[0]] = item.split(":")[1]
	else:
		passports.append({})
		i += 1

n = 0

for j in range(len(passports)):
	try:
		print(passports[j]["byr"])
		print(passports[j]["iyr"])
		print(passports[j]["eyr"])
		print(passports[j]["hgt"])
		print(passports[j]["hcl"])
		print(passports[j]["ecl"])
		print(passports[j]["pid"])
		#print(passports[j]["cid"])
		n += 1
		print("Valid!")
	except:
		print("Invalid!")

print(n)