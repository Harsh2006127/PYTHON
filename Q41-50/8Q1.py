class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

p1 = Person("Harsh", 18, 5.8, 65)
p2 = Person("Aman", 19, 5.6, 60)

print("Person 1:")
print(p1.name, p1.age, p1.height, p1.weight)

print("\nPerson 2:")
print(p2.name, p2.age, p2.height, p2.weight)