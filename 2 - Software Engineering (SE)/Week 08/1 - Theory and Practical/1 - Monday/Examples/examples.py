def sum_list(num_list):
    total = 0
    for num in num_list:
        if not isinstance(num, (int, float)):
            return None
        total += num
    return total


def get_middle_of_list(lst):
    if lst:
        mid_index = len(lst)//2
        return lst[mid_index]
    return None


def get_average(grades):
    return sum(grades)/len(grades)

def get_all_students_average(student_grades):
    if student_grades:
        grade_average = 0
        for grades in student_grades:
            grade_average += get_average(grades)
        grade_average = round(grade_average/len(student_grades), 2)
        return grade_average
    return 0


def recursive_word_flip(word):
    if len(word) <= 1:
        return word
    else:
        # Add index to word
        return recursive_word_flip(word[1:]) + word
