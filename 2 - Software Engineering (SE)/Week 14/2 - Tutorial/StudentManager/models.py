from sqlalchemy import Column, String, Integer, Date, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class BaseModel(Base):
    """Base model for other models."""
    __abstract__ = True
    __allow__unmapped__ = True

    id = Column("id", Integer, autoincrement=True, primary_key=True)

class Grade(BaseModel):
    """Model representing a subject and grade for a particular student."""
    __tablename__ = "Grades"

    student_id = Column(ForeignKey('Students.id'))
    subject = Column(String)
    grade = Column(Integer)

    def __repr__(self):
        return f"<{self.subject} - {self.grade}%>"

class Student(BaseModel):
    """Model representing the data of a student."""
    __tablename__ = "Students"

    name = Column('name', String)
    surname = Column('surname', String)
    date_of_birth = Column('address', Date)
    email = Column('email', String)
    phone_number = Column("phone_number", String)
    grades = relationship(Grade)

    def __str__(self):
        output = f"Student ID:\t{self.id}\nFull Name:\t{self.name} {self.surname}\n"
        output += f"Date of Birth:\t{self.date_of_birth}\nEmail:\t\t{self.email}\n"
        output += f"Phone Number:\t{self.phone_number}\nGrades:\n\n"
        for grade in self.grades:
            output += f"{grade.subject}: {grade.grade}%\n"
        return output

    def __repr__(self):
        return f"<{self.id} - ({self.name} {self.surname}) {self.grades = }>"



def build_tables(engine):
    """Build tables without database migration"""
    Base.metadata.create_all(bind=engine)
