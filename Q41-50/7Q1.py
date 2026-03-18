file = open("name.txt", "w")
file.write("Aman\nRohit\nIshita\nKaran\nOm\n")
file.close()

file = open("name.txt", "r")
names = file.readlines()

names = [name.strip() for name in names]

print("Total names:", len(names))

vowels = "AEIOUaeiou"
count = 0
for name in names:
    if name[0] in vowels:
        count += 1

print("Names starting with vowel:", count)

longest = names[0]
for name in names:
    if len(name) > len(longest):
        longest = name

print("Longest name:", longest)

file.close()