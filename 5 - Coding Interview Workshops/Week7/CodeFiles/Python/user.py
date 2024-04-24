class User:
    def __init__(self, username, password, accessCode):
        self.username = username
        self._password = password
        self._accessCode = accessCode

    def getAccess(self, username, password):
        if (self.username == username):
            if (self._password == password):
                return self._accessCode
            else:
                return "Incorrect Password"
        else:
            return "Incorrect Username"
        
        
        
    