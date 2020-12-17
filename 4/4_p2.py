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

		byr_valid = int(passports[j]["byr"]) >= 1920 and int(passports[j]["byr"]) <= 2002
		iyr_valid = int(passports[j]["iyr"]) >= 2010 and int(passports[j]["iyr"]) <= 2020
		eyr_valid = int(passports[j]["iyr"]) >= 2020 and int(passports[j]["iyr"]) <= 2030
		ecl_valid = passports[j]["ecl"] == "amb" or passports[j]["ecl"] == "blu" or passports[j]["ecl"] == "brn" or passports[j]["ecl"] == "gry" or passports[j]["ecl"] == "grn" or passports[j]["ecl"] == "hzl" or passports[j]["ecl"] == "oth"


		if passports[j]["hgt"][-1] == "m":
			hgt_valid = int(passports[j]["hgt"][0:3]) >= 150 and int(passports[j]["hgt"][0:3]) <= 193
		elif passports[j]["hgt"][-1] == "n":
			hgt_valid = int(passports[j]["hgt"][0:2]) >= 59 and int(passports[j]["hgt"][0:2]) <= 76
		else:
			raise

		hcl_valid = passports[j]["hcl"][0] == "#"
		pid_valid = len(passports[j]["pid"]) == 9

		for k in passports[j]["hcl"]:
			if k not in "#0123456789abcdef":
				hcl_valid = False
			else:
				continue

		print(passports[j]["byr"])
		print(byr_valid)
		print(passports[j]["iyr"])
		print(iyr_valid)
		print(passports[j]["eyr"])
		print(eyr_valid)
		print(passports[j]["hgt"])
		print(hgt_valid)
		print(passports[j]["hcl"])
		print(hcl_valid)
		print(passports[j]["ecl"])
		print(ecl_valid)
		print(passports[j]["pid"])
		print(pid_valid)

		if byr_valid and iyr_valid and eyr_valid and ecl_valid and hgt_valid and hcl_valid and pid_valid:
			n += 1
			print("Valid!")
		else:
			print("Invalid!")
	except:
		print("Invalid!")

print(n)