import unittest
from examples import sum_list, get_middle_of_list, get_all_students_average


class TestExamples(unittest.TestCase):

    # sum_list
    def test_sum_list_with_one_value(self):
        value = [7]
        result = sum_list(value)
        self.assertEqual(result, 7)

    def test_sum_list_with_two_values(self):
        values = [7, 13]
        result = sum_list(values)
        self.assertEqual(result, 20)

    def test_sum_list_with_invalid_values(self):
        values = ["a", 13]
        result = sum_list(values)
        self.assertEqual(result, None)

    # Get_middle_list
    def test_get_mid_value_with_one_value(self):
        test_list = [5]
        result = get_middle_of_list(test_list)
        self.assertEqual(result, 5)

    def test_get_mid_value_with_no_values(self):
        test_list = []
        result = get_middle_of_list(test_list)
        self.assertEqual(result, None)

    def test_get_mid_value_with_three_values(self):
        test_list = [5, 4, 8, 19]
        result = get_middle_of_list(test_list)
        self.assertEqual(result, 8)

    def test_grade_average_with_no_students(self):
        test_grades = []
        result = get_all_students_average(test_grades)
        self.assertEqual(result, 0)

    def test_grade_average_with_1_students(self):
        test_grades = [[50, 50, 50]]
        result = get_all_students_average(test_grades)
        self.assertEqual(result, 50)

    def test_grade_average_with_multiple_students(self):
        test_grades = [[20, 50, 70], [80, 60, 50], [70, 60, 60], [50, 60, 40]]
        result = get_all_students_average(test_grades)
        self.assertEqual(result, 55.83)

class TestRecursiveFlip(unittest.TestCase):
    pass

if __name__ == "__main__":
    unittest.main()