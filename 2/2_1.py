f = open("input.txt", "r")

n = 0

for i in f:
    inp = i.split()
    pwd = inp[2]
    characters = inp[0].split("-")
    letter = inp[1][0]
    count = pwd.count(letter)

    letters = ["", ""]
    
    try:
        letters[0] = pwd[int(characters[0])-1]
    except:
        letters[0] = ""

    try:
        letters[1] = pwd[int(characters[1])-1]
    except:
        letters[1] = ""

    sol = 0
    
    if letter == letters[0]:
        sol += 1

    if letter == letters[1]:
        sol += 1
    
    if sol == 1:
        n += 1
        print("Valid! " + str(n) + " | " + i)
        print(letter)
        print(letters)
        print(pwd)
    else:
        print("Invalid" + " | " + i)
        print(letter)
        print(letters)
        print(pwd)
