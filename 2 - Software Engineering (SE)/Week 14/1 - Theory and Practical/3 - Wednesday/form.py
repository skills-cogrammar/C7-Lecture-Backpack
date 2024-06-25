# Should be run independently
# python form.py

from tkinter import *
from models import User, Comment, Profile
from orm_engine import session

# Create the main window
window = Tk()
window.title("LinkedOut")

def clear():
    [widget.delete(0, END) for widget in window.winfo_children() if isinstance(widget, Entry)]


def save_entry():
  """get entry from the user and store them in the database
  """
  try:

    # Create Comment, Profile, and User objects
    comment = Comment(comment=comment_entry.get())
    profile = Profile(profile=job_title_entry.get())
    age = int(age_entry.get())
    name = name_entry.get()
    user = User(name=name, age=age, profile=profile, comment=comment)
    session.add(user)
    session.commit()
  except:
      session.rollback()
      raise
  else:
      session.commit()
  # Clears the screen
  clear()


# Create labels for input fields
name_field = Label(window, text="Name:")
name_field.grid(row=0, column=0)

age_field = Label(window, text="Age:")
age_field.grid(row=1, column=0)

profile_field = Label(window, text="Job Title:")
profile_field.grid(row=2, column=0)

comment_filed = Label(window, text="LinkOut Comment:")
comment_filed.grid(row=3, column=0)

# Create entry fields for user input
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

age_entry = Entry(window)
age_entry.grid(row=1, column=1)

job_title_entry = Entry(window)
job_title_entry.grid(row=2, column=1)

comment_entry = Entry(window)
comment_entry.grid(row=3, column=1)

# Create a button to trigger storing 
button = Button(window, text="Save", command=save_entry)
button.grid(row=4, columnspan=2)

# Run the main loop
window.mainloop()