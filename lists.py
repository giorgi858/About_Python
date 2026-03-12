my_list = []

for first_list in range(10):
    my_info = { 'name': 'giorgi', 'lastname': 'mtsituri' }
    my_list.append(my_info)


for begining_list in my_list[:3]:
    print(begining_list)

print('....')


#############

original_list = []
for x in range(1, 11):
    square = x ** 2
    original_list.append(square)

print(original_list)
