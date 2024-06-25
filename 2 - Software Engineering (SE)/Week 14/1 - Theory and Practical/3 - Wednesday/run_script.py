# Should be run independently
# python run_script.py

from sqlalchemy import select
from models import User, Comment, Profile
from orm_engine import session

while True:
    # Get user information
    user_name = input("Enter your name (or 'q' to quit): ")
    comment_text = input("Enter your linkedout comment (or 'q' to quit): ")
    profile_text = input("What's your current job ? (or 'q' to quit): ")
    age = int(input("How old are you ? (or '0' to quit): "))

    # Check for quit option
    if user_name.lower() == 'q':
        break

    try:
        # Create Comment, Profile, and User objects
        comment = Comment(comment=comment_text)
        profile = Profile(profile=profile_text)
        user = User(name=user_name, age=age, profile=profile, comment=comment)

        # Print the created user data (replace with actual database interaction)
        print(f"Created User:")
        print(f"  Name: {user.name}")
        print(f"  Age: {user.age}")
        print(f"  Profile: {user.profile.profile}")
        print(f"  Comment: {user.comment.comment}")

        print("\n---\n")  # Separator between users
        session.add(user)
        session.commit()
    except:
        session.rollback()
        raise
    else:
        session.commit()