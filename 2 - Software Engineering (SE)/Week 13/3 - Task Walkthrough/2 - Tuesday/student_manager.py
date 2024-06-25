class StudentManager:

    def __init__(self) -> None:
        self.students = []

    def add_student(self, student):
        if self.get_student(student.id):
            return
        self.students.append(student)

    def get_student(self, id):
        for student in self.students:
            if student.id == id:
                return student
            
    def remove_student(self, id):
        for i in range(len(self.students)):
            if self.students[i].id == id:
                del self.students[i]

                
class Student:

    def __init__(self, id, name, surname, address=""):
        self.id = id
        self.name = name
        self.surname = surname
        self.address = address
        self.grades = {}

    def add_grade(self, subject, grade):
        if isinstance(subject, str) and isinstance(grade, (int, float)):
            self.grades[subject] = grade

    def get_grade_average(self):
        grade_total = 0
        if not self.grades:
            return
        for grade in self.grades.values():
            grade_total += grade
        return grade_total/len(self.grades)
