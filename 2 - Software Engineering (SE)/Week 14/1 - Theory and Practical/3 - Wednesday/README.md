# Building a Simple ORM in Python Using SQLAlchemy

This guide will walk you through the process of creating a simple Object-Relational Mapping (ORM) system using SQLAlchemy 2.0 in Python. ORM allows you to interact with your database using Python objects, making your code cleaner and easier to maintain.

## Table of Contents
1. [Setting Up Your Environment](#1-setting-up-your-environment)
2. [Installing SQLAlchemy 2.0](#2-installing-sqlalchemy-20)
3. [Creating the ORM Script](#3-creating-the-orm-script)
4. [Setting Up the SQLAlchemy Engine](#4-setting-up-the-sqlalchemy-engine)
5. [Establishing a Session](#5-establishing-a-session)
6. [Defining the Base Class](#6-defining-the-base-class)
7. [Creating ORM Mapped Classes](#7-creating-orm-mapped-classes)
8. [Performing Database Operations](#8-performing-database-operations)
9. [Running Your ORM Script](#9-running-your-orm-script)
10. [Conclusion](#10-conclusion)

## 1. Setting Up Your Environment

First, we'll create a virtual environment to manage our project's dependencies. This keeps your project isolated and avoids conflicts with other Python packages.

```bash
# Create a virtual environment named 'env'
python -m venv orm_venv

# Activate the virtual environment
# On Windows
orm_venv\Scripts\activate
# On MacOS/Linux
source orm_venv/bin/activate
```

## 2. Installing SQLAlchemy 2.0

With your virtual environment active, install SQLAlchemy 2.0. This version includes several enhancements over previous versions.

```bash
pip install sqlalchemy
```

or to be more specific:

```bash
pip install sqlalchemy==2.0.*
```
The current code is built on the basis of SQLAlchemy 2.0. It may fail when using SQLAlchemy 1.x. 

## 3. Creating the ORM Script

Create a new Python file named `orm_script.py` where we will write our ORM code.

In your linux system, including MacOs:
```bash
touch orm_script.py
```
or create this file on Windows.

In this file, we'll include all the code necessary to set up and use our ORM.

## 4. Setting Up the SQLAlchemy Engine

The engine is the core of SQLAlchemy's connection to your database. It manages the connections and interactions with the database backend. 

```python
from sqlalchemy import create_engine

# Example using SQLite
engine = create_engine('sqlite:///example.db', echo=True)

# Example using PostgreSQL
# engine = create_engine('postgresql://user:password@localhost/mydatabase')

# Example using MySQL
# engine = create_engine('mysql+pymysql://user:password@localhost/mydatabase')

# Example using Oracle
# engine = create_engine('oracle+cx_oracle://user:password@localhost/mydatabase')
```

The `echo=True` parameter will output the generated SQL queries to the console, which is useful for debugging.

## 5. Establishing a Session

The session is the interface to the database. It allows you to query, add, update, and delete objects from the database.

```python
from sqlalchemy.orm import Session

# Create a Session instance
session = Session()
```

## 6. Defining the Base Class

The base class is the foundation for all our ORM-mapped classes. It provides the framework for table and class definitions.

```python
from sqlalchemy.orm import declarative_base

# Create a base class for our classes to inherit
Base = declarative_base()
```

## 7. Creating ORM Mapped Classes

Define your database models by creating classes that inherit from the `Base` class. Each class represents a table in your database.

### Entity Relationship Diagram of the exercise: One to One: 

Check the One-to-One relationship : [SQLAlchemy One-to-One](https://docs.sqlalchemy.org/en/20/orm/basic_relationships.html#one-to-one)

![image](images/ERD.png)

```python
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String

class User(Base):
    __tablename__ = "user_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]  = mapped_column(String(30))
    age: Mapped[int] = mapped_column(Integer)

    comment: Mapped["Comment"] = relationship(back_populates="user")
    profile: Mapped["Profile"] = relationship(back_populates="user")

    def __repr__(self):
        return f"<User(name={self.name}, age={self.age})>"
```

### Explanation of User Model Attributes and Relationships

The `User` class defines the structure of a user record in your database. Let's break down the key aspects:

**Table and Columns:**

- `__tablename__ = "user_table"`: This specifies the name of the table that will be created in your database to store user information.

- **Basic User Attributes:**

    - `id: Mapped[int] = mapped_column(primary_key=True)`: This defines the `id` column for each user. It's an integer (`int`) and is set as the primary key (`primary_key=True`), ensuring each user has a unique identifier.
    - `name: Mapped[str] = mapped_column(String(30))`: This defines the `name` column, storing the user's name as a string (`str`) with a maximum length of 30 characters (`String(30)`).
    - `age: Mapped[int] = mapped_column(Integer)`: This defines the `age` column, storing the user's age as an integer (`int`).

**Relationships: `comment` and `profile`**

These columns are particularly interesting as they represent relationships between the `User` model and other models in your database. Let's delve deeper:

- `comment: Mapped["Comment"] = relationship(back_populates="user")`:
    - This defines a one-to-many relationship between a `User` and their associated `Comment` objects. It means one user can have multiple comments.
    - `Mapped["Comment"]`: This specifies that the `comment` attribute will hold references to `Comment` objects.
    - `relationship(back_populates="user")`: This creates a bidirectional relationship. When accessing a user's `comment` attribute, you'll retrieve their comments. Conversely, within the `Comment` model, there's likely a `user` attribute that references the user who wrote the comment (using `back_populates="user"`).

- `profile: Mapped["Profile"] = relationship(back_populates="user")`:
    - This defines a one-to-one relationship between a `User` and their `Profile` information. Each user has a single profile.
    - `Mapped["Profile"]`: Similar to `comment`, this indicates the `profile` attribute will hold a reference to a `Profile` object.
    - `relationship(back_populates="user")`: Again, this establishes a bidirectional relationship. Accessing a user's `profile` attribute retrieves their profile information, and the `Profile` model likely has a `user` attribute referencing the associated user (using `back_populates="user"`).

By defining these relationships, you're telling SQLAlchemy how to manage the connections between users, comments, and profiles in your database. This allows you to easily retrieve related data in a single query.


Then you have: 

```python
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Integer, String, ForeignKey

class Profile(Base):
    __tablename__ = "profile_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    profile: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship("User", back_populates="profile")

    def __repr__(self):
        return f"{self.profile}"
    

class Comment(Base):
    __tablename__ = "comment_table"
    id: Mapped[int] = mapped_column(primary_key=True)
    comment: Mapped[str]  = mapped_column(String(30))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))
    user: Mapped['User'] = relationship(back_populates="comment")

    def __repr__(self):
        return f"{self.comment}"
```

### Explanation of Profile and Comment Models

**Profile Model:**

The `Profile` class defines the structure for storing user profile information in your database.

- **Table and Column:**

    - `__tablename__ = "profile_table"`: This specifies the table name in the database to store profile data.

- **Profile Information:**

    - `id: Mapped[int] = mapped_column(primary_key=True)`: The `id` column acts as the primary key, uniquely identifying each profile record.
    - `profile: Mapped[str] = mapped_column(String(30))`: This column stores the user's profile information as a string (`str`), with a maximum length of 30 characters (`String(30)`).

- **Foreign Key Relationship:**

    - `user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))`: This creates a foreign key constraint. It ensures the `user_id` in the `Profile` table references a valid `id` in the `user_table`. This establishes a one-to-one relationship between a `User` and their `Profile`.
    - In simpler terms, each profile belongs to exactly one user.

- **Relationship with User:**

    - `user: Mapped['User'] = relationship("User", back_populates="profile")`: This defines a bidirectional relationship with the `User` model.
        - `Mapped['User']`: The `user` attribute will hold a reference to a `User` object.
        - `relationship("User", back_populates="profile")`: Establishes a connection between `Profile` and `User`. When accessing a user's `profile` attribute, you'll retrieve their profile information. Conversely, the `User` model likely has a `profile` attribute referencing the associated profile (using `back_populates="profile"`).

**Comment Model:**

The `Comment` class defines the structure for storing user comments in your database.

- **Table and Column:**

    - `__tablename__ = "comment_table"`: This specifies the table name in the database to store user comments.

- **Comment Information:**

    - `id: Mapped[int] = mapped_column(primary_key=True)`: The `id` column acts as the primary key, uniquely identifying each comment record.
    - `comment: Mapped[str] = mapped_column(String(30))`: This column stores the user's comment as a string (`str`), with a maximum length of 30 characters (`String(30)`).

- **Foreign Key Relationship:**

    - `user_id: Mapped[int] = mapped_column(ForeignKey("user_table.id"))`: Similar to the `Profile` model, this creates a foreign key constraint, ensuring the `user_id` in the `Comment` table references a valid `id` in the `user_table`. This establishes a one-to-many relationship between a `User` and their associated comments.
    - In simpler terms, one user can have multiple comments.

- **Relationship with User:**

    - `user: Mapped['User'] = relationship("User", back_populates="comment")`: This defines a bidirectional relationship with the `User` model.
        - `Mapped['User']`: The `user` attribute will hold a reference to a `User` object.
        - `relationship("User", back_populates="comment")`: Establishes a connection between `Comment` and `User`. When accessing a user's `comment` attribute, you'll retrieve their comments. Conversely, the `User` model likely has a `comment` attribute referencing the associated comments (using `back_populates="comment"`).

By defining these relationships, you're enabling SQLAlchemy to manage the connections between users, profiles, and comments effectively. You can efficiently retrieve related data in a single query, simplifying your database interactions.


## 8. Performing Database Operations

Create, query, update, and delete operations are done through the session. Here’s how you can perform basic CRUD operations:

### Create Tables

First, you need to create the tables in your database:

```python
# Create all tables in the engine (equivalent to "Create Table" in SQL)
Base.metadata.create_all(engine)
```

### Add New Records

To add a new user to the database:

```python
new_user = User(name='Alice', age=30)
session.add(new_user)
session.commit()
```

### Query Records

To query users from the database:

```python
# Query all users
users = session.execute(select(User)).all()
print(users)

# Query a user by name
alice = session.execute(select(User).where(User.name=="Alice")).first()
print(alice)
```

### Update Records

To update an existing user's information:

```python
statement_update = update(User).values({"age": "70"}).where(User.name=="Nick")
session.execute(statement_update)
session.commit()
```

### Delete Records

To delete a user from the database:

```python
from sqlalchemy import delete
# delete row
statement_delete = delete(User).where(User.name == 'Maxim')
session.execute(stmt)
session.commit()
```

## 9. Running Your ORM Script

Now that we have our ORM defined and can interact with our database, you can run your script:

```bash
python orm_script.py
```

## 10. Conclusion

You have successfully created a simple ORM in Python using SQLAlchemy 2.0. This guide has covered the basics of setting up your environment, defining ORM classes, and performing CRUD operations. Explore further to understand advanced topics such as relationships, eager loading, and more.

---