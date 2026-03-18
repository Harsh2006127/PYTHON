n = int(input("Enter number of fruits: "))

s1 = set(input("Enter fruits of set1: ").split())
s2 = set(input("Enter fruits of set2: ").split())

print("Common fruits:", s1 & s2)
print("Only in s1:", s1 - s2)
print("Total fruits count:", len(s1 | s2))
