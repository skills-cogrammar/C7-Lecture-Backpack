from utils import draw_line

def view_posts(posts):
    template = ""
    for i, post in enumerate(posts, 1):
        template += draw_line()
        template += f"{i} {post.get_user()}: {post.get_title()} | {post.get_content()[:40]}\n"
    template += draw_line()
    print(template)
    index = input("Please choose a post to view('0' to go back): ")
    return index

def view_post(post):
    template = draw_line()
    template += f"{post.get_user()}: {post.get_title()}\n"
    template += draw_line()
    post_content = post.get_content()
    for i in range(0, len(post_content)+80, 80):
        template += f"{post_content[i:i+80]}\n"
    template += draw_line()
    print(template)


def login_menu():
    while True:
        user_input = input("""Please choose an option below: 
                1. Login
                2. Create New User

                0. Quit
                : """)
        if user_input in ["0", "1", "2"]:
            return user_input


def get_user_details(register=False):
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    if register:
        password_conf = input("Please confirm your password: ")
        return (username, password, password_conf)
    return (username, password)

def get_post_content():
    title = input("Post Title:\n")
    content = input("Enter post:\n")
    return (title, content)

def main_menu(user):
    menu = f"Welcome {user.get_name()}\n"
    menu += "Please select an option below:\n\n"
    menu += "1. Make Post\n"
    menu += "2. View Posts\n\n"
    menu += "0. Quit\n:"
    return menu
