""" ======= Create the SQLite Database and Tables with sqlite script """

# ***** The Library.db database
import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('Library.db')

# Create a cursor object
cur = conn.cursor()
# conn.close()                # remove the close to run the rest of the code.

# ===== SQL script to create the Authors table
create_authors_table_sql = """
CREATE TABLE IF NOT EXISTS Authors (
    author_id INTEGER PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    birthdate DATE NOT NULL,
    country VARCHAR(50) NOT NULL
);
"""

# Execute the SQL scripts
cur.execute(create_authors_table_sql)

# Commit the changes and close the connection
conn.commit()

# ===== SQL script to create the Books table
create_books_table_sql = """
CREATE TABLE IF NOT EXISTS Books (
    book_id INTEGER PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(30) NOT NULL,
    published_date DATE NOT NULL,
    author_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);
"""

# Execute the SQL scripts
cur.execute(create_books_table_sql)

# Commit the changes and close the connection
conn.commit()

# You can continue with the above format of entering the query into a variable,
# then execute the variable query and commit.

# conn.close()
# Remember to close the database if you only want to create tables

""" There are easier ways to complete this task
1.) Go to https://sqliteonline.com/
OR
2.) Download the DB Browser from https://sqlitebrowser.org/
"""

""" Populate the tables """
# Grab query portion only for sqlinteonline.com or sqlitebrowser.org

# ===== SQL script to insert data into Authors table
insert_authors_data_sql = """
INSERT OR IGNORE INTO Authors (author_id, first_name, last_name, birthdate, country) VALUES
(1, 'Emma', 'Smith', '1985-03-12', 'UK'),
(2, 'James', 'Johnson', '1978-08-25', 'UK'),
(3, 'Sophie', 'Williams', '1990-05-20', 'UK'),
(4, 'David', 'Brown', '1982-11-08', 'UK'),
(5, 'John', 'Doe', '1970-01-15', 'USA'),
(6, 'Jane', 'Lee', '1982-09-30', 'USA'),
(7, 'Maria', 'Garcia', '1988-06-05', 'Spain'),
(8, 'Hans', 'Mueller', '1975-04-18', 'Germany')
;
"""

# Execute the SQL scripts
cur.execute(insert_authors_data_sql)

# Commit the changes and close the connection
conn.commit()

# ===== SQL script to insert data into Books table
insert_books_data_sql = """
INSERT OR IGNORE INTO Books (book_id, title, genre, published_date, author_id) VALUES
(1, 'Pride and Prejudice', 'Romance', '1813-01-28', 1),
(2, 'Great Expectations', 'Novel', '1861-08-01', 2),
(3, 'Harry Potter and the Philosopher''s Stone', 'Fantasy', '1997-06-26', 3),
(4, 'The Hitchhiker''s Guide to the Galaxy', 'Science Fiction', '1979-10-12', 4),
(5, 'To Kill a Mockingbird', 'Fiction', '1960-07-11', 5),
(6, '1984', 'Dystopian', '1949-06-08', 5),
(7, 'The Catcher in the Rye', 'Coming-of-age', '1951-07-16', 6),
(8, 'Don Quixote', 'Adventure', '1605-01-16', 7),
(9, 'Faust', 'Tragedy', '1808-12-30', 8),
(10, 'The Casual Vacancy', 'Drama', '2012-09-27', 1)
;
"""

# Execute the SQL scripts
cur.execute(insert_books_data_sql)

# Commit the changes and close the connection
conn.commit()

"""
Comparison of INNER JOIN with LEFT OUTER JOIN:
INNER JOIN: Only includes rows with matching values in both tables.
LEFT OUTER JOIN: Includes all rows from the left table and 
the matched rows from the right table. 
If there is no match, the result is NULL for columns from the right table.

FROM OUR PDF NOTES:
LEFT OUTER joins are similar to INNER joins. Like the INNER join, it will use
a specified column to match values across two tables. There is just one small
distinction. Let's say that you are using a LEFT OUTER join on Table A and
Table B. Column X is the common column between the two tables. If there is a
value in X for Table A that doesn't exist in Table B, it will still show in
the output (but with rows in the Table B columns just showing null values).
"""
"""
INNER JOIN:
This join returns only the rows where there is a match in both tables.
Query Purpose: This query lists the first names and last names of
all students who are enrolled in the course with the course code 'DS03'.
Process: It joins the Student and Course tables on the stu_subject_code
and course_code columns. It then filters the results to include only
the rows where the course_code is 'DS03'.
"""

# ===== SQL Script to list the titles of all books written by authors from the UK.
select_uk_books_sql = """
SELECT title
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.author_id
WHERE Authors.country = 'UK'
;
"""

# Execute the SQL scripts
cur.execute(select_uk_books_sql)

# Fetch the results
rows = cur.fetchall()

# Display the results
print("\n===== select_uk_books_sql =====")
for row in rows:
    print(row)

# ===== SQL script to list the first names and last names of all authors from
# the UK, along with the genres of the books they have written.

uk_authors_by_genre_sql = """
SELECT Authors.first_name, Authors.last_name, Books.genre
FROM Authors
INNER JOIN Books ON Authors.author_id = Books.author_id
WHERE Authors.country = 'UK'
;
"""

# Execute the SQL scripts
cur.execute(uk_authors_by_genre_sql)

# Fetch the results
rows = cur.fetchall()

# Display the results
print("\n===== uk_authors_by_genre_sql =====")
for row in rows:
    print(row)

# ===== SQL script to list the titles of all books published
# by UK authors after the year 2000.

books_published_after_2000_sql = """
SELECT title
FROM Books
INNER JOIN Authors ON Books.author_id = Authors.author_id
WHERE Authors.country = 'UK' AND Books.published_date > '2000-01-01'
;
"""

# Execute the SQL scripts
cur.execute(books_published_after_2000_sql)

# Fetch the results
rows = cur.fetchall()

# Display the results
print("\n===== books_published_after_2000_sql =====")
for row in rows:
    print(row)

# ===== SQL script to list the first names and last names of
# UK authors who have written more than one book, along with the
# count of books they have written.

uk_authors_and_books_count_sql = """
SELECT Authors.first_name, Authors.last_name, COUNT(Books.book_id) as book_count
FROM Authors
INNER JOIN Books ON Authors.author_id = Books.author_id
WHERE Authors.country = 'UK'
GROUP BY Authors.author_id
HAVING COUNT(Books.book_id) > 1
;
"""

# Execute the SQL scripts
cur.execute(uk_authors_and_books_count_sql)

# Fetch the results
rows = cur.fetchall()

# Display the results
print("\n===== uk_authors_and_books_count_sql =====")
for row in rows:
    print(row)

""" ===== LEFT OUTER JOIN example """
# This query lists the first names and last names of all authors from the UK,
# along with the titles of the books they have written (if any).

uk_authors_with_books_loj_sql = """
SELECT Authors.first_name, Authors.last_name, Books.title
FROM Authors
LEFT OUTER JOIN Books ON Authors.author_id = Books.author_id
WHERE Authors.country = 'UK'
;
"""

# Execute the SQL scripts
cur.execute(uk_authors_with_books_loj_sql)

# Fetch the results
rows = cur.fetchall()

# Display the results
print("\n===== uk_authors_with_books_loj_sql =====")
for row in rows:
    print(row)

"""
In this query:

We select the first_name and last_name columns from the Authors table.
We also select the title column from the Books table.

We use a LEFT OUTER JOIN to join the Authors and Books tables on
the author_id column. The LEFT OUTER JOIN ensures that all authors from
the UK are included in the result set, regardless of whether they
have written any books.

We filter the results to include only authors from the UK using
the country = 'UK' condition in the WHERE clause.
"""
