class User {
    constructor (username, password, accessCode) {
        this.username = username
        this._password = password
        this._accessCode = accessCode
    }ƒ

    getAccess(username, password) {
        if (this.username == username) {
            if (this._password == password)
                return this._accessCode;
            else
                return "Incorrect Password";
        }
        else
            return "Incorrect Username";
    }
}       
        
        
    