from hashlib import sha1
from views import view_posts, view_post, login_menu, main_menu, get_user_details, get_post_content
from models import Post, User

class Controller:

    def __init__(self):
        self.__current_user = None

    def start(self):
        while self.__current_user is None:
            user_option = login_menu()
            if user_option == "1":
                self.__login()
            elif user_option == "2":
                self.__create_user()
            elif user_option == "0":
                break
        while self.__current_user:
            self.__main_menu()

    def __login(self):
        username, password = get_user_details()
        user = User.get_user(username)
        if user and user.check_password(sha1(password.encode("utf-8")).hexdigest()):
            self.__current_user = user

    def __main_menu(self):
        option = input(main_menu(self.__current_user))
        if option == "1":
            self.__make_post()
        elif option == "2":
            self.__get_all_posts()
        elif option == "0":
            exit()

    def __make_post(self):
        title, content = get_post_content()
        new_post = Post(self.__current_user.get_name(), title, content)
        new_post.save()
        view_post(new_post)

    def __get_all_posts(self):
        posts = Post.get_posts()
        while True:
            user_index = view_posts(posts)
            if not user_index.isdigit():
                continue
            if user_index == "0":
                return
            user_index = int(user_index)
            if 0 < user_index <= len(posts):
                break
            print("Invalid input!")
        view_post(posts[user_index-1])

    def __create_user(self):
        while True:
            username, password, password_conf = get_user_details(register=True)
            if username in User.usernames():
                print("Username taken!")
                continue
            if password == password_conf:
                break
            print("Passwords don't match. Please Try again.")

        new_user = User(username, sha1(password.encode(encoding="utf-8")).hexdigest())
        new_user.set_name(username)
        new_user.save()
        self.__current_user = new_user
