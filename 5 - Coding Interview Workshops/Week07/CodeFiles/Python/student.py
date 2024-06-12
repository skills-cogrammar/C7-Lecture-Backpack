class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def sayMyName (self):
        print("Hi, my name is " + self.name)

zahra = Student("Zahra", 23, 12)
print(zahra.name)

