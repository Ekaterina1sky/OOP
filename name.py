class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, rate):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.rates:
                lecturer.rates[course] += [rate]
            else:
                lecturer.rates[course] = [rate]
        else:
            return 'Ошибка'

    def average_score(self):
        middle_sum = 0
        for course_grades in self.grades.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки нет'
        else:
            return f'{middle_sum / len(self.grades.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname} \n'
        res += f'Средняя оценка за домашние задания: {self.average_score()} \n'
        res += f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)} \n'
        res += f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, student):
        if not isinstance(student, Student):
            print(f'Такого студента нет')
            return
        return self.average_score() < student.average_score()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.rates = {}


class Lecturer(Mentor):
    def middle_rate(self):
        middle_sum = 0
        for course_grades in self.rates.values():
            course_sum = 0
            for grade in course_grades:
                course_sum += grade
            middle_of_course = course_sum / len(course_grades)
            middle_sum += middle_of_course
        if middle_sum == 0:
            return f'Оценки нет'
        else:
            return f'{middle_sum / len(self.rates.values()):.2f}'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        res += f'Средняя оценка {self.middle_rate()}\n'
        return res

    def __lt__(self, lecturer):
        if not isinstance(lecturer, Lecturer):
            print(f' Такого лектора нет')
            return
        return self.middle_rate() < lecturer.middle_rate()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name} \nФамилия: {self.surname}\n'
        return res


def grades_students(students_list, course):
    overall_student_rating = 0
    lectors = 0
    for listener in students_list:
        if course in listener.grades.keys():
            average_student_score = 0
            for grades in listener.grades[course]:
                average_student_score += grades
            overall_student_rating = average_student_score / len(listener.grades[course])
            average_student_score += overall_student_rating
            lectors += 1
    if overall_student_rating == 0:
        return f'Оценок нет'
    else:
        return f'{overall_student_rating / lectors:.2f}'


def grades_lecturers(lecturer_list, course):
    average_rating = 0
    b = 0
    for lecturer in lecturer_list:
        if course in lecturer.rates.keys():
            lecturer_average_rates = 0
            for rate in lecturer.rates[course]:
                lecturer_average_rates += rate
            overall_lecturer_average_rates = lecturer_average_rates / len(lecturer.rates[course])
            average_rating += overall_lecturer_average_rates
            b += 1
    if average_rating == 0:
        return f'Оценок нет'
    else:
        return f'{average_rating / b:.2f}'


st1 = Student('Петя', 'Петров', 'your_gender')
st1.finished_courses = ['Python', 'C++']
st1.courses_in_progress = ['Git', 'Java']

st2 = Student('Иван', 'Иванов', 'your_gender')
st2.finished_courses = ['С++', 'Git']
st2.courses_in_progress = ['Python', 'Java']
st_list = [st1, st2]

lec1 = Lecturer('Саша', 'Сушков')
lec1.courses_attached = ['Git', 'Java']

lec2 = Lecturer('Вася', 'Васильков')
lec2.courses_attached = ['Python']
lec_list = [lec1, lec2]

rev1 = Reviewer('Паша', 'Пашков')
rev1.courses_attached = ['Python', 'С++', 'Java', 'Git']

rev2 = Reviewer('Толя', 'Тольков')
rev2.courses_attached = ['Git', 'Python', 'С++']

rev1.rate_hw(st1, 'Git', 9)
rev1.rate_hw(st1, 'Git', 7)
rev1.rate_hw(st1, 'Git', 10)
rev1.rate_hw(st1, 'Java', 5)
rev1.rate_hw(st1, 'Java', 8)
rev1.rate_hw(st1, 'Java', 9)
rev1.rate_hw(st1, 'Python', 9)
rev1.rate_hw(st1, 'Python', 3)
rev1.rate_hw(st1, 'Python', 2)
rev1.rate_hw(st1, 'С++', 10)
rev1.rate_hw(st1, 'С++', 9)
rev1.rate_hw(st1, 'С++', 4)

rev2.rate_hw(st2, 'С++', 4)
rev2.rate_hw(st2, 'С++', 2)
rev2.rate_hw(st2, 'С++', 3)
rev2.rate_hw(st2, 'Git', 8)
rev2.rate_hw(st2, 'Git', 1)
rev2.rate_hw(st2, 'Git', 7)
rev2.rate_hw(st2, 'Python', 8)
rev2.rate_hw(st2, 'Python', 10)
rev2.rate_hw(st2, 'Python', 5)
rev2.rate_hw(st2, 'Java', 7)
rev2.rate_hw(st2, 'Java', 4)
rev2.rate_hw(st2, 'Java', 10)

st1.rate_lecturer(lec1, 'Git', 10)
st1.rate_lecturer(lec1, 'Git', 5)
st1.rate_lecturer(lec1, 'Git', 9)
st1.rate_lecturer(lec1, 'Java', 6)
st1.rate_lecturer(lec1, 'Java', 7)
st1.rate_lecturer(lec1, 'Java', 8)

st2.rate_lecturer(lec1, 'Java', 10)
st2.rate_lecturer(lec1, 'Java', 9)
st2.rate_lecturer(lec1, 'Java', 10)
st2.rate_lecturer(lec2, 'Python', 10)
st2.rate_lecturer(lec2, 'Python', 2)
st2.rate_lecturer(lec2, 'Python', 8)

print(st1)
print(st2)

# if st1 > st2:
#     print(f'{st1.name} учится лучше чем {st2.name}')
# else:
#     print(f'{st2.name} учится лучше чем {st1.name}')

print(rev1)
print(rev2)

print(lec1)
print(lec2)

# if lec1 > lec2:
#     print(f'{lec1.name, lec1.surname} преподает лучше чем {lec2.name, lec2.surname}')
# else:
#     print(f'{lec2.name, lec2.surname} преподает лучше чем {lec1.name, lec1.surname}')

print(f'Средняя оценка студентов по курсу "Git": {grades_students(st_list, "Git")}')
print(f'Средняя оценка студентов по курсу "Java": {grades_students(st_list, "Java")}')
print(f'Средняя оценка студентов по курсу "Python": {grades_students(st_list, "Python")}')

print(f'Средняя оценка лекторов по курсу "Git": {grades_lecturers(lec_list, "Git")}')
print(f'Средняя оценка лекторов по курсу "Java": {grades_lecturers(lec_list, "Java")}')
print(f'Средняя оценка лекторов по курсу "Python": {grades_lecturers(lec_list, "Python")}')
