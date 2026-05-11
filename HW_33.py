class Person:
    def __init__(self, name):
        self.name = name
        
    def introduce(self):
        print(f"Hello, my name is {self.name}")
        
class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)  # вызываем родительский __init__
        self.course = course
   
    def introduce(self):
        print(f"I'm on course {self.course}")   

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # вызываем родительский __init__
        self.subject = subject
   
    def introduce(self):
        print(f"Hello, I am professor  {self.name}. \nMy subject is {self.subject}")   
     
user = Person("Alice")
user.introduce()
# user1 = Student("Alice",2)
# user1.introduce()

staff = [Student("Alice",2), Teacher("Bob", "Mathematics")]

for person in staff:
    person.introduce() 
    print("-----")
