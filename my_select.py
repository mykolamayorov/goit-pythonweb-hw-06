from sqlalchemy import func, desc, Numeric
from app.db.database import SessionLocal
from app.models import Student, Group, Teacher, Subject, Grade


def select_1():
    session = SessionLocal()
    result = session.query(
        Student.name,
        func.round(func.avg(Grade.grade).cast(Numeric), 2).label("avg_grade")
    ).join(Grade)\
     .group_by(Student.id)\
     .order_by(desc("avg_grade"))\
     .limit(5)\
     .all()
    session.close()
    return result


def select_2(subject_name):
    session = SessionLocal()
    result = session.query(
        Student.name,
        func.avg(Grade.grade).label("avg_grade")
    ).select_from(Grade)\
     .join(Student)\
     .join(Subject)\
     .filter(Subject.name == subject_name)\
     .group_by(Student.id)\
     .order_by(desc("avg_grade"))\
     .first()
    session.close()
    return result


def select_3(subject_name):
    session = SessionLocal()
    result = session.query(
        Group.name,
        func.avg(Grade.grade)
    ).select_from(Grade)\
     .join(Student)\
     .join(Group)\
     .join(Subject)\
     .filter(Subject.name == subject_name)\
     .group_by(Group.id)\
     .all()
    session.close()
    return result


def select_4():
    session = SessionLocal()
    result = session.query(func.avg(Grade.grade)).scalar()
    session.close()
    return result


def select_5(teacher_name):
    session = SessionLocal()
    result = session.query(Subject.name)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name)\
        .all()
    session.close()
    return result


def select_6(group_name):
    session = SessionLocal()
    result = session.query(Student.name)\
        .join(Group)\
        .filter(Group.name == group_name)\
        .all()
    session.close()
    return result


def select_7(group_name, subject_name):
    session = SessionLocal()
    result = session.query(Student.name, Grade.grade)\
        .join(Grade)\
        .join(Group)\
        .join(Subject)\
        .filter(Group.name == group_name)\
        .filter(Subject.name == subject_name)\
        .all()
    session.close()
    return result


def select_8(teacher_name):
    session = SessionLocal()
    result = session.query(func.avg(Grade.grade))\
        .select_from(Grade)\
        .join(Subject)\
        .join(Teacher)\
        .filter(Teacher.name == teacher_name)\
        .scalar()
    session.close()
    return result


def select_9(student_name):
    session = SessionLocal()
    result = session.query(Subject.name)\
        .select_from(Grade)\
        .join(Subject)\
        .join(Student)\
        .filter(Student.name == student_name)\
        .distinct()\
        .all()
    session.close()
    return result


def select_10(student_name, teacher_name):
    session = SessionLocal()
    result = session.query(Subject.name)\
        .select_from(Grade)\
        .join(Subject)\
        .join(Student)\
        .join(Teacher, Subject.teacher_id == Teacher.id)\
        .filter(Student.name == student_name)\
        .filter(Teacher.name == teacher_name)\
        .distinct()\
        .all()
    session.close()
    return result


if __name__ == "__main__":
    print(select_1())