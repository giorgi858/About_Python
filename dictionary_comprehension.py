numb = {number: number**3 for number in range(1, 21)}
print("dictionary comprehension - ", numb)


numbers_second = [x * 2 for x in numb]
print("list comprehension - ", numbers_second)