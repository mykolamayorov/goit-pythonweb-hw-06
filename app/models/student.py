from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    group_id = Column(Integer, ForeignKey("groups.id"))

    group = relationship("Group", backref="students")
    grades = relationship("Grade", backref="student")