prompt = 'Please enter the name of city you have vizited: 😊 (Enter quit when you are finished.)\n'

cities_user_is_visited = []

while True:
    city = input(prompt)
    if city.lower() == 'quit':
        break
    elif city.lower() ==  'paris':
        paris_city = f'{city.title()} is beautiful city especial in sprig'
        print(paris_city)
        cities_user_is_visited.append(city.title())
    else:
        print(f'{city.title()} is great one')
        cities_user_is_visited.append(city.title())


with open ('city.txt', 'a') as file:
    for city in cities_user_is_visited:
        file.write(city + '\n')
            