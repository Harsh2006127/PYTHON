start = int(input("Enter starting value: "))
end = int(input("Enter ending value: "))

print("Even numbers:")
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i, end=" ")

print("\nOdd numbers:")
for i in range(start, end + 1):
    if i % 2 != 0:
        print(i, end=" ")
