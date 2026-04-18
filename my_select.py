from sqlalchemy import func, desc, Numeric
from app.db.database import SessionLocal
from app.models import Student, Group, Teacher, Subject, Grade

session = SessionLocal()

def select_1():
    return session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade).group_by(Student.id)\
     .order_by(desc("avg_grade")).limit(5).all()

def select_2(subject_name):
    return session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).select_from(Grade)\
     .join(Student)\
     .join(Subject)\
     .filter(Subject.name == subject_name)\
     .group_by(Student.id)\
     .order_by(desc("avg_grade"))\
     .first()

def select_3(subject_name):
    return session.query(
        Group.name,
        func.avg(Grade.grade)
    ).select_from(Grade)\
     .join(Student)\
     .join(Group)\
     .join(Subject)\
     .filter(Subject.name == subject_name)\
     .group_by(Group.id)\
     .all()

def select_4():
    return session.query(func.avg(Grade.grade)).scalar()

def select_5(teacher_name):
    return session.query(Subject.name)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name).all()

def select_6(group_name):
    return session.query(Student.name)\
        .join(Group)\
        .filter(Group.name == group_name).all()

def select_7(group_name, subject_name):
    return session.query(Student.name, Grade.grade)\
        .join(Grade)\
        .join(Group)\
        .join(Subject)\
        .filter(Group.name == group_name)\
        .filter(Subject.name == subject_name)\
        .all()

def select_8(teacher_name):
    return session.query(func.avg(Grade.grade))\
        .select_from(Grade)\
        .join(Subject)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name)\
        .scalar()

def select_9(student_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .filter(Student.name == student_name).distinct().all()

def select_10(student_name, teacher_name):
    return session.query(Subject.name)\
        .join(Grade)\
        .join(Student)\
        .join(Teacher, Subject.teacher_id == Teacher.id)\
        .filter(Student.name == student_name)\
        .filter(Teacher.name == teacher_name)\
        .distinct().all()

session.close()

if __name__ == "__main__":
    print(select_1())