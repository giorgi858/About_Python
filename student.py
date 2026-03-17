from person import Person
class Student(Person):
    def __init__(self, full_name, age, house, gpa):
        self.gpa = gpa
        super().__init__(full_name, age, house)
        
    def student_GPA(self):
        print(f"{self.full_name}'s GPA is : {self.gpa}")
        
    
student = Student('nino samkharadze', 32, 'No', 2.1)

student.persons_full_name()
student.persons_age()
student.own_the_house()
student.student_GPA()