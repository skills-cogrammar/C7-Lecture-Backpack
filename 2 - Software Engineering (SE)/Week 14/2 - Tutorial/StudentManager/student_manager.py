from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Grade
import settings

class StudentManager:
    """Class repsonsible for managing our models and interactions with our models."""

    def __init__(self) -> None:
        self.engine = create_engine(settings.DB_ADDRESS)

    @property
    def get_session(self):
        """Create new session with current engine."""
        return sessionmaker(bind=self.engine)()

    def add_student(self, name, surname, date_of_birth, email, phone_number):
        """Creates a new student model and adds new student to database.
        
        Parameters
        ----------
        name : str
            Name of new student.
        surname : str
            Surname of new student.
        date_of_birth : Date
            Date of birth of new student.
        email : str
            Email of new student.
        phone_number : str
            Phone Number of new student."""
        new_student = Student(name=name,
                              surname = surname,
                              date_of_birth = date_of_birth,
                              email = email,
                              phone_number = phone_number)
        with self.get_session as session:
            session.add(new_student)
            session.commit()

    def remove_student(self, student_id):
        """Removes student with given ID from database.
        
        Parameters
        ----------
        student_id : int
            ID of student to be removed."""
        with self.get_session as session:
            session.query(Student).filter(Student.id == student_id).delete()
            session.commit()

    def get_student(self, student_id):
        """Gets student with given ID from database and returns a string representation.
        
        Parameters
        ----------
        student_id : int
            ID of student to be removed.
            
        Returns
        -------
        String representation of student with given ID."""
        with self.get_session as session:
            result = session.query(Student).filter(Student.id == student_id).first()
            return str(result)
        
    def update_student_email(self, student_id, new_email):
        """Updates email address of student with given ID"""
        with self.get_session as session:
            student = session.query(Student).filter(Student.id == student_id).first()
            student.email = new_email
            session.query(Student).filter(Student.id == student_id).first()
            session.commit()

    def view_all_students(self):
        """Retrieve all student from database and print a basic string representation."""
        with self.get_session as session:
            result = session.query(Student).all()
            for student in result:
                print(f"{student.id} - {student.name} {student.surname}")

    def add_grade(self, student_id, subject, grade):
        """Creates a new grade for a given student.
        
        Parameters
        ----------
        student_id: int
            ID of student to add grade to.
        subject : str
            Name of the subject the grade is for.
        grade : int
            Grade score student achieved for subject."""
        new_grade = Grade(student_id=student_id, subject=subject, grade=grade)
        with self.get_session as session:
            result = session.query(Student).filter(Student.id == student_id).first()
            if result:
                session.add(new_grade)
                session.commit()
