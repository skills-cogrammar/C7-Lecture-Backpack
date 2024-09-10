from file_access import FileAccess

class AuthService:
    def __init__(self, file_name):
        self.__data_storage = FileAccess(file_name)

    def login(self, email: str, password: str):
        users = self.__data_storage.read()

        password = self.__hash_password(password)

        for user in users:
            if user["email"] == email:
                return user["password"] == password

        return False

    def sign_up(self, user_details: dict):
        self.__validate_sign_up_input(user_details)
        
        user_details["password"] = self.__hash_password(user_details["password"])

        self.__data_storage.write(user_details)
    
    def __validate_sign_up_input(self, user_details):
        if (not user_details.get("email")):
            raise Exception("Email address required")

        if (not user_details.get("password")):
            raise Exception("Password required")        

    def __hash_password(self, password: str):        
        return hash(password)
