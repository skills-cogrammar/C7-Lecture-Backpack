#Class method
class Student:
    school_name = 'St Patrick primary'

    def __init__(self,name,age):
        self.name = name
        self.age = age

    #class method, cls == original class
    @classmethod
    def change_school(cls,school_name):
        #class_name.class_variable 
        cls.school_name = school_name

    #instance method
    def show_results(self):
        print(self.name,self.age, 'School: ', Student.school_name)

#Create an instance of class Student
s1 = Student("Charlie",11)
s1.show_results() 

#Change school_name
Student.change_school('St John')
s1.show_results()