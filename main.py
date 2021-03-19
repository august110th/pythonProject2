
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lector(self, lecturer, course, grade):
        if isinstance(
                lecturer, Lecturer
        ) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        print("print(some_student)")
        print(f"Имя: {self.name}")
        print(f"Фамилиия: {self.surname}")


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(
                student, Student
        ) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        print("print(some_reviewer)")
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}
    def __str__(self):
        print("print(some_lecturer)")
        print(f"Имя: {self.name}")
        print(f"Фамилия: {self.surname}")

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

worst_student = Student("Petr", "Ivanov", "male")
worst_student.courses_in_progress += ["Git"]

middle_student = Student("Jack", "Daniels", "male")
middle_student.courses_in_progress += ["Python", "Git"]

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

usual_reviewer = Reviewer("Phil", "Collins")
usual_reviewer.courses_attached += ["Git"]

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(middle_student, "Python", 8)
cool_reviewer.rate_hw(middle_student, "Python", 7)
cool_reviewer.rate_hw(middle_student, "Python", 9)
usual_reviewer.rate_hw(worst_student, "Git", 4)
usual_reviewer.rate_hw(worst_student, "Git", 5)
usual_reviewer.rate_hw(worst_student, "Git", 4)

cool_lecturer = Lecturer("Ivan", "Petrov")
cool_lecturer.courses_attached += ['Python']

bad_lecturer = Lecturer("Mick", "Jagger")
bad_lecturer.courses_attached += ["Git"]

best_student.rate_lector(cool_lecturer, "Python", 10)
best_student.rate_lector(cool_lecturer, "Python", 9)
best_student.rate_lector(cool_lecturer, "Python", 10)
worst_student.rate_lector(bad_lecturer, "Git", 2)
worst_student.rate_lector(bad_lecturer, "Git", 5)
worst_student.rate_lector(bad_lecturer, "Git", 6)

# print(cool_lecturer.grades)
# print(middle_student.grades)

for key, value in middle_student.grades.items():
    print(sum(value) / len(value))

lecturer_grades = []
student_grades = []
student_grades.append(best_student.grades)
student_grades.append(middle_student.grades)
student_grades.append(worst_student.grades)
lecturer_grades.append(cool_lecturer.grades)
lecturer_grades.append(bad_lecturer.grades)

print(student_grades)
print(lecturer_grades)
# for key, value in lecturer_grades:
#     print(key)
# def course_stat(student):
#   if isinstance(student, Student) and course in student.courses_in_progress:
bad_lecturer.__str__()
