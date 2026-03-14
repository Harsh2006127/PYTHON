n = int(input("Enter the value of n: "))

if n < 0:
    print("Please enter a positive integer.")
else:
    total_sum = n * (n + 1) // 2
    print(f"The sum of the first {n} natural numbers is: {total_sum}")