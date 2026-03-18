file = open("numbers.txt", "w")
file.write("45\n120\n67\n300\n150\n90\n")
file.close()

file = open("numbers.txt", "r")

numbers = []

for line in file:
    numbers.append(int(line.strip()))

print("Maximum number:", max(numbers))

average = sum(numbers) / len(numbers)
print("Average:", average)

count = 0
for num in numbers:
    if num > 100:
        count += 1

print("Numbers greater than 100:", count)

file.close()