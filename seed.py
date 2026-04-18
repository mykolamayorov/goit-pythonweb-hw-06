import random
from datetime import datetime, timedelta

from faker import Faker

from app.db.database import SessionLocal
from app.models import Group, Student, Teacher, Subject, Grade

fake = Faker()

session = SessionLocal()


# -------------------
# CREATE GROUPS
# -------------------
groups = [Group(name=f"Group-{i}") for i in range(1, 4)]
session.add_all(groups)
session.commit()


# -------------------
# CREATE TEACHERS
# -------------------
teachers = [Teacher(name=fake.name()) for _ in range(random.randint(3, 5))]
session.add_all(teachers)
session.commit()


# -------------------
# CREATE SUBJECTS
# -------------------
subjects_list = [
    "Math", "Physics", "Chemistry", "Biology",
    "History", "English", "Programming", "Databases"
]

subjects = []
for name in random.sample(subjects_list, random.randint(5, 8)):
    subjects.append(
        Subject(
            name=name,
            teacher_id=random.choice(teachers).id
        )
    )

session.add_all(subjects)
session.commit()


# -------------------
# CREATE STUDENTS
# -------------------
students = []

for _ in range(random.randint(30, 50)):
    student = Student(
        name=fake.name(),
        group_id=random.choice(groups).id
    )
    students.append(student)

session.add_all(students)
session.commit()


# -------------------
# CREATE GRADES
# -------------------
for student in students:
    for _ in range(random.randint(10, 20)):
        grade = Grade(
            student_id=student.id,
            subject_id=random.choice(subjects).id,
            grade=round(random.uniform(60, 100), 2),
            date_received=datetime.now() - timedelta(days=random.randint(0, 365))
        )
        session.add(grade)

session.commit()


session.close()

print("Database successfully seeded!")