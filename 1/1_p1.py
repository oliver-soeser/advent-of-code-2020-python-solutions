f = open("input.txt", "r")

numbers = []

for i in f:
    numbers.append(int(i))


for i in range(len(numbers)):
    for j in range(len(numbers)):
        if ((numbers[i] + numbers[j]) == 2020):
            print(str(numbers[i]) + " + " + str(numbers[j]) + " = 2020")
            print("Answer: " + str(numbers[i]*numbers[j]))
