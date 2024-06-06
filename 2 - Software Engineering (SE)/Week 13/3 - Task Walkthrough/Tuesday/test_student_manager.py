import unittest
from student_manager import Student, StudentManager

class TestStudent(unittest.TestCase):

    def setUp(self) -> None:
        # Arrange
        self.student = Student(0, "Peter", "Parker")

    def test_adding_a_grade_to_student(self):
        # Act
        self.student.add_grade("Maths", 70)
        # Assert
        self.assertEqual(self.student.grades, {"Maths":70})

    def test_adding_grade_with_incorrect_input(self):
        self.student.add_grade(45, 70)
        self.assertEqual(self.student.grades, {})

    def test_get_grade_average(self):
        # Arrange
        self.student.add_grade("Maths", 70)
        self.student.add_grade("Physics", 75)
        self.student.add_grade("Biology", 65)
        # Act
        result = self.student.get_grade_average()
        # Assert
        self.assertEqual(result, 70)

    def test_get_grade_with_no_subjects(self):
        result = self.student.get_grade_average()
        self.assertEqual(result, None)


class TestStudentManager(unittest.TestCase):

    def setUp(self) -> None:
        self.student_manager = StudentManager()

    def test_adding_student_to_manager(self):
        new_student = Student(1, "James", "Parker")
        self.student_manager.add_student(new_student)
        self.assertListEqual(self.student_manager.students, [new_student])

    def test_adding_users_with_same_id(self):
        student1 = Student(1, "Tina", "Tinason")
        student2 = Student(1, "John", "Johnson")
        self.student_manager.add_student(student1)
        self.student_manager.add_student(student2)
        self.assertListEqual(self.student_manager.students, [student1])
    