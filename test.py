import math
# Data types - strings, ints, floats, booleans, NoneType, complex  
# data types are value of a variable
# Data structures - lists, tuples , sets, dictionary, list comprehensions, dictionary comprehensions
string = 'this is a string'
integer = 2
boolean = bool(2> 3)
# print(boolean) 
float_number = 2.2
lits  = [ 1,2, "other", True ]
dictionary = {
    'name': "giorgi",
    'lastname': "mtsituri",
    'age': 28
}
# Control Flow
# if and else  
# we have two main type of loops, while loops and for loops
# while loop
# number = 0
# while number <= 5:
#     print(number)
#     number += 1
    
# print(number)

# for loop

# loops with index
# for index, element in enumerate(lits):
#     print(index, element)
    
# for i in range(10):
#     print(i)

# for letter in "new letter":
#     print(letter)

    
# for i in range(20):
#     if i ==15:
#         break
#     print(i)


# for i in range(20):
#     if i ==15:
#         continue
#     print(i)

# for i in range(4):
#     print(i)
# else:
#     print('finished')

#dictionary loops
# for key, value in dictionary.items():
#     my_info = f' My Info - {key}: {value}' 
#     print(my_info)

# list comprehension

# numbers =  [i*2 for i in range(4)]
# print(numbers)

# print(type(True))

# def math_example(*args, **kwargs):
#     if kwargs['operation'] == 'sum':
#         print(sum(args))
#         return sum(args)
#     if kwargs['operation'] == 'multiply' and kwargs['message'] == 'success':
#         print(math.prod(args))
#         return  math.prod(args)
        
#     else:
#         return print('We have an Error')
    
# math_example(2,100, operation='multiply', message='success')


# original_list = []

# numb = {number: number**2 for number in range(1, 21)}
# print(numb)

# # numbers = [x * 2 for x in randome_numb]
# # original_list.append(numbers)
# # print(original_list)

# for x in range(1, 11):
#     square = x ** 2
#     original_list.append(square)

# print(original_list)


# my_list = []

# for first_list in range(10):
#     my_info = { 'name': 'giorgi', 'lastname': 'mtsituri' }
#     my_list.append(my_info)


# for begining_list in my_list[:3]:
#     print(begining_list)

# print('....')
