class Person():
    def __init__(self, full_name, age, house):
        self.full_name = full_name
        self.age = age
        self.house = house
        self.Welcome_message = 'Welcome Everyone'
        
    def persons_full_name(self):
        full_name = f'Persons full name is - {self.full_name.title()}.'
        print(full_name)
    
    def persons_age(self):
        if self.age < 18:
            print('You are younger person.')
        elif self.age <=30:
            print('you are middle age.')
        elif self.age <= 50:
            print('You are grown person.')
        else:
            print('you are old enogh to make some important decision.')
                
        
    def own_the_house(self):
        if self.house.lower() == 'yes':
            print(f'{self.full_name.title()} own the house')
        elif self.house.lower() == 'no':
            print(f'{self.full_name.title()} does not have a their own house')
            