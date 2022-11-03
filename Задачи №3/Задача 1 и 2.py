from asyncio.windows_events import NULL
from functools import reduce
import math
from unittest import result


class Course:
    def __init__(self, name='', grade=2.0):
        self.__name = name
        self.__grade = grade
    
    @property
    def name(self):
        return self.__name
    
    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, new_grade):
        self.__grade = new_grade

class Student:
    def __init__(self, name, student_id_number, year):
        self.__name = name
        self.__student_id_number = student_id_number
        self.__year = year
        self.__courses = []
    
    @property
    def name(self):
        return self.__name

    @property
    def student_id_number(self):
        return self.__student_id_number

    @property
    def year(self):
        return self.__year

    @property
    def courses(self):
        return self.__courses

    def start_new_year(self):
        self.__year += 1
        self.__courses = []
    
    def add_new_course(self, course):
        self.__courses.append(course)

    def password_decorator(f):
        def inner(something):
            result = NULL
            input_password = input("Enter the hidden password:")
            if input_password == "super_safe_password":
                result = f(something)
            else: 
                print("Sorry the password is incorrect") 

            return result 

        return inner

    @password_decorator
    def get_good_students(students):
        return [student.name for student in students 
        if (reduce(lambda acc, course: acc + course.grade, student.courses, 0) / len(student.courses)) >= 4.50]


student_1 = Student('Ivan the Programmer', '12345', 1)
student_1.add_new_course(Course('Algebra', 4.50))
student_1.add_new_course(Course('Intro to programming', 6.00))
student_1.add_new_course(Course('Geometry', 3.00))
student_1.add_new_course(Course('Calculus', 2.00))

student_2 = Student('Maria', '12346', 1)
student_2.add_new_course(Course('Algebra', 5.75))
student_2.add_new_course(Course('Intro to programming', 6.00))
student_2.add_new_course(Course('Geometry', 6.00))
student_2.add_new_course(Course('Calculus', 6.00))

student_3 = Student('Gosho from break', '12347', 1)
student_3.add_new_course(Course('Algebra', 2.00))
student_3.add_new_course(Course('Intro to programming', 2.00))
student_3.add_new_course(Course('Geometry', 2.00))
student_3.add_new_course(Course('Calculus', 3.00))

students_list = [student_1, student_2, student_3]

print(Student.get_good_students(students_list))
# print(Student.get_good_students(students_list))
# print(Student.get_good_students(students_list))

