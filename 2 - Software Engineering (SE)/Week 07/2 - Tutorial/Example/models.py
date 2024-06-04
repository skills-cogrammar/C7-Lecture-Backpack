import sqlite3

class Model:
    _connection = sqlite3.connect("data.db")

    def save(self):
        pass

    def update(self):
        pass


class User(Model):

    def __init__(self, username, password) -> None:
        self.__username = username
        self.__password = password
        self.__name = ""
        self.__surname = ""
        self.__about = ""

    def get_username(self):
        return self.__username

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        self.__name = new_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__name = new_surname

    def get_about(self):
        return self.__about

    def set_about(self, new_about):
        self.__name = new_about

    def check_password(self, password):
        return self.__password == password

    def update_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password

    def save(self):
        query = "INSERT INTO Users VALUES ('{}', '{}', '{}', '{}', '{}')".format(self.__username,
                                                                                 self.__password,
                                                                                 self.__name,
                                                                                 self.__surname,
                                                                                 self.__about)
        self._connection.execute(query)
        self._connection.commit()

    def update(self, **values):
        query = "UPDATE Users SET "
        for key, value in values.items():
            if key not in vars(self).keys():
                print(f"{key} is not an attribute of User!")
                return
            query += f"{key} = '{value}',"
        query = query.strip(",")
        query += f" WHERE username = '{self.__username}'"
        self._connection.execute(query)
        self._connection.commit()

    @staticmethod
    def usernames():
        cursor = User._connection.execute("SELECT username FROM Users;")
        usernames = []
        for username in cursor:
            usernames.append(username[0])
        return usernames

    @staticmethod
    def get_user(username):
        cursor = User._connection.execute("Select * from Users WHERE username = '{}'"
                                            .format(username))
        user_data = list(cursor)
        if user_data:
            user_data = user_data[0]
            user = User(user_data[0], user_data[1])
            user.set_name(user_data[2])
            user.set_surname(user_data[3])
            user.set_about(user_data[4])
            return user
        print("User does not exist!")
        return None


class Admin(User):
    pass


class Post(Model):

    def __init__(self, user, title, content) -> None:
        self.user = user
        self.title = title
        self.content = content

    def get_user(self):
        return self.user

    def get_title(self):
        return self.title

    def set_title(self, new_title):
        self.title = new_title

    def get_content(self):
        return self.content

    def set_content(self, new_content):
        self.content = new_content

    @staticmethod
    def get_posts():
        cursor = Post._connection.execute("Select * from Posts")
        posts = []
        for post in cursor:
            posts.append(Post(post[0], post[1], post[2]))
        return posts

    def save(self):
        query = f"INSERT INTO Posts VALUES ('{self.user}', '{self.title}', '{self.content}')"
        self._connection.execute(query)
        self._connection.commit()

    def __str__(self):
        return f"{self.user}\n{self.title}: {self.content[:25]}"
