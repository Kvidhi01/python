# python code to print the smallest number in the list
lst = (20, 10, 20, 1, 100)
print(min(lst, key=lambda value: int(value)))