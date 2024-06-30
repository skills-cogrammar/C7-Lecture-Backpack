const mongoose = require("mongoose");
const bcrypt = require("bcrypt");
const SALT = 10;

/*
    We are using mongoose to act as a validation layer in our code 
    By setting additional paramters to the fields, we can be sure that
    the data being passed to the database is safe and won't negatively affect 
    our application.

    Input validation is a very important aspect of securing an application.
*/


const authSchema = mongoose.Schema({
    email: {
        type: String,
        required: true,
        unique: true,
        lowercase: true,
        trim: true,
        match: [/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/, 'Please fill a valid email address']
    },
    password: {
        type: String,
        required: true,
        minlength: 6,
        select: false
    },
    role: {
        type: String,
        enum: ["user", "admin"],
        default: "user"
    },
    isActive: {
        type: Boolean,
        default: true
    }    
});


// Mongoose includes the `pre` method which allows us to add some logic on certain 
// operations.
// The pre-save will run certain code before our object is saved in the database 
// in this instance, we are using the pre-save to hash the users password 
// If there are any issues with the password, we will go to the next piece of middleware
authSchema.pre("save", function (next) {
    if (!this.isModified("password")) return next();

    bcrypt.hash(this.password, SALT, (err, hash) => {
        if (err) return next(err);
        this.password = hash;
        next();
    });
});

// We can also add methods to the mongoose model
// This will it easier to do object specific operations without writing additonal 
// logic in other parts of our applications
//
// The following method is taking the password that a user enters 
// when trying to login and compares the hashed version of that password 
// to the hashed version of the password that is stored in our database 
// if they match, a success message will be passed otherwise an error is sent back
authSchema.methods.comparePassword = function (candidatePassword, cb) {
    bcrypt.compare(candidatePassword, this.password, (err, isMatch) => {
        if (err) return cb(err);
        cb(null, isMatch);
    });
};

module.exports = mongoose.model("Auth", authSchema);