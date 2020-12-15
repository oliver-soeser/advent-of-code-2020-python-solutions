start = [2, 20, 0, 4, 1, 17]

ncache = dict()

i = 1
n = start[-1]

for s in start[:-1]:
	ncache[s] = i
	i += 1

i += 1

while i <= 2020:
	if n not in ncache:
		ncache[n] = i-1
		n = 0
	else:
		d = i - 1 - ncache[n]
		ncache[n] = i - 1
		n = d
	i += 1

print(n)