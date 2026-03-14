num = int(input("enter a number: "))
shift = int(input("enter number of bits of shift :"))
left_shift = num << shift
right_shift = num >> shift
print(" left shift value :", left_shift)
print(" right shift value :", right_shift)