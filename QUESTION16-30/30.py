def second_largest(lst):
    lst = list(set(lst))
    lst.sort()
    return lst[-2]

print(second_largest([10, 20, 5, 40, 30]))