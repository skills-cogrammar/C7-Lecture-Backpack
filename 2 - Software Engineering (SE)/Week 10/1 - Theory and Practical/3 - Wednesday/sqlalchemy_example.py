from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a SQLite database engine
engine = create_engine('sqlite:///example.db')

# Create a base class for declarative ORM models
Base = declarative_base()

# Define a database model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create tables in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Insert data into the table
user = User(name='John', age=30)
session.add(user)
session.commit()

# Close the session
session.close()
