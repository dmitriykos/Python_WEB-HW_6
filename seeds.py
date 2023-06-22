from datetime import datetime, date, timedelta
from random import randint

from faker import Faker

from connection import create_connection, Error

fake = Faker('uk-UA')

disciplines = [
    "Програмування",
    "Теорія струн",
    "Математичний аналіз",
    "Висшая математика",
    "Аналітична алгебра",
    "Креслення",
    "Теоретична механніка",
    "Фізика твердого тіла",
    "Векторна алгебра"
]

groups = ['МТ-03-2', 'ФП-03-2', 'МІ-02-1']

NUMBERS_TEACHERS = 5
NUMBERS_STUDENTS = 50


def seed_teacher():
    teachers = [fake.name() for _ in range(NUMBERS_TEACHERS)]
    sql_ex = "INSERT INTO teachers(fullname) VALUES (%s);"
    cur.executemany(sql_ex, zip(teachers,))


def seed_groups():
    sql_ex = "INSERT INTO groups(name) VALUES (%s);"
    cur.executemany(sql_ex, zip(groups,))


def seed_disciplines():
    list_teacher_id = [randint(1, NUMBERS_TEACHERS) for _ in range(len(disciplines))]
    sql_ex = "INSERT INTO disciplines(name, teacher_id) VALUES (%s, %s);"
    cur.executemany(sql_ex, zip(disciplines, iter(list_teacher_id)))


def seed_students():
    students = [fake.name() for _ in range(NUMBERS_STUDENTS)]
    list_group_id = [randint(1, len(groups)) for _ in range(NUMBERS_STUDENTS)]
    sql_ex = "INSERT INTO students(fullname, group_id) VALUES (%s, %s);"
    cur.executemany(sql_ex, zip(students,iter(list_group_id)))


def seed_grades():
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-06-30", "%Y-%m-%d")

    sql_ex = "INSERT INTO grades(student_id, discipline_id, grade, date_of) VALUES (%s, %s, %s, %s);"


    def get_list_of_date(start_date, end_date):
        result = []
        current_date: date = start_date
        while current_date <= end_date:
            if current_date.isoweekday() < 6:
                result.append(current_date)
            current_date += timedelta(1)
        return result

    list_dates = get_list_of_date(start_date, end_date)

    grades = []
    for day in list_dates:
        random_discipline = randint(1, len(disciplines))
        random_students = [randint(1, NUMBERS_STUDENTS) for _ in range(5)]
        for student in random_students:
            grades.append((student, random_discipline, randint(1, 12), day.date()))
    cur.executemany(sql_ex, grades)


if __name__ == "__main__":
    with create_connection() as connect:
        cur = connect.cursor()
        seed_teacher()
        seed_groups()
        seed_disciplines()
        seed_students()
        seed_grades()
        connect.commit()
