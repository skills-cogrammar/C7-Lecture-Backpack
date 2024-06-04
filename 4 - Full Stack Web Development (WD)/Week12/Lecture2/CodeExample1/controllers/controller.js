const modelFile = require('../models/userModel');
const userModel = modelFile.userModel;
const jwt = require("jsonwebtoken");

// Login
const loginUser = async (req, res) => {
    const {username, password, admin} = req.body;
    const user = await userModel.find({username: username, password: password});

    if (user.length == 1) {
        const payload = {
            "name": username,
            "password": password,
            "admin": admin
        }

        const token = jwt.sign(JSON.stringify(payload),
                                "lecture-1-secret",
                                {algorithm: 'HS256'});

        res.send({
            message: "Admin Login Successful",
            token: token
        });

    } else {
        res.status(401).send({
            "message": "User does not exist"
        })
    }
}

// Access Resource


// Add New Admin User
const createAdminUser = async (req, res) => {
    const { username, password } = req.body;
    const user = await userModel.create({
        username: username,
        password: password,
        admin: true
    });
    const savedUser = await user.save();
    res.json({
        "message": "New User Created Successfully!",
        "savedUser": savedUser
    })
}

// Export
module.exports = {
    loginUser,
    createAdminUser
};