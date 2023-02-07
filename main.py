import os

from utils import get_student_by_pk, get_profession_by_title, check_fitness

# path_student = os.path.join('data', 'students.json')
# path_professions = os.path.join('data', 'professions.json')

number_student = int(input("Введите номер студента: ").capitalize().strip())
student = get_student_by_pk(number_student)

print(f"Студент {student['full_name']}")
print(f"Знает {' '.join(student['skills'])}")

professions_student = input(f"Выберите специальность для оценки студента {student['full_name']}: ").capitalize().strip()
professions = get_profession_by_title(professions_student)

check = check_fitness(student['skills'], professions['skills'])
print(f"Пригодность: {check['fit_percent']}")
print(f"{student['full_name']} знает {' '.join(check['has'])}")
print(f"{student['full_name']} не знает {' '.join(check['lacks'])}")


# Программа: Jane Snake знает Python, Linux
# Программа: Jane Snake не знает Docker, SQL
#
# # Пользователь: Backend
