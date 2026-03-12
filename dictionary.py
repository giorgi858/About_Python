
vano_info = {'name': 'vano', 'lastname': 'kharanauli', 'age': 27}
giorgi_info = {'name': 'giorgi', 'lastname': 'mtsituri', 'age': 28}
vasiko_info = {'name': 'vasiko', 'lastname': 'mtsituri', 'age': 29}

my_list = [vano_info, giorgi_info, vasiko_info]

for info in my_list:
    print(info)
info = [] 
my_info = ''
cities = {
    'tbilisi ': {'population': 1200000, 'capital': True },
    'kutaisi': {'population': 50000, 'capital ': False},
    'rustavi': {'population': 30000, 'capital ': False},
    }
for city,city_info in cities.items():
    for key, value in city_info.items():
        my_info = f'{value}'
        info.append(my_info)


print(info)
