from sqlalchemy import Column, Integer, Float, Date, ForeignKey
from app.db.database import Base


class Grade(Base):
    __tablename__ = "grades"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"))
    subject_id = Column(Integer, ForeignKey("subjects.id"))

    grade = Column(Float, nullable=False)
    date_received = Column(Date, nullable=False)