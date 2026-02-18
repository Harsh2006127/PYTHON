
fruits = ["apple", "banana", "mango"]
print("Initial fruits list:", fruits)

fruits.append("orange")
print("After adding a fruit:", fruits)

fruits.remove("banana")
print("After removing a fruit:", fruits)

search = input("Enter a fruit to search: ")
if search in fruits:
    print("Fruit Found")
else:
    print("Fruit Not Found")

print("Number of fruits:", len(fruits))

fruits.sort()
print("Sorted fruits:", fruits)

fruits.reverse()
print("Reversed fruits:", fruits)

print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

fruit_tuple = tuple(fruits)
print("Fruits tuple:", fruit_tuple)

print("Count of apple in tuple:", fruit_tuple.count("apple"))

print("All fruits:")
for f in fruit_tuple:
    print(f)