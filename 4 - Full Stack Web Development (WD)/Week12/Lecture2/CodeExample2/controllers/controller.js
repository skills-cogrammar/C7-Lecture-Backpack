const { User } = require("../models/Users");
const jwt = require("jsonwebtoken")

const getHomePath = (req, res) => {
  res.json({
    message: "Hello World",
  });
};

//C(CREATE: User)
const createUser = async (req, res) => {
  const { username, password, admin } = req.body;
  try {
    const createdUser = await User.create({
      username,
      password,
      admin,
    });
    const user = await createdUser.save();
    res.json({
      message: "User created Successfully",
      user,
    });
  } catch (err) {
    console.log(err);
    res.json(err);
  }
};

//R(READ: Users)
const getAllUsers = async (req, res) => {
  try {
    const users = await User.find();
    res.send({
      message: "Users fetched",
      users: users,
    });
  } catch (err) {
    console.log(err);
  }
};

//Login(Login a users)
const loginUser = async (req, res)=>{
    const { username, password } = req.body

    try {
        const foundUser = await User.findOne({username: username, password: password})
        if ( foundUser ) {
            const payload = {
                admin: foundUser.admin,
                username: foundUser.username
            }

            const token = jwt.sign(payload, "secret", {algorithm: "HS256"})

            res.json({
                message: "Login Successfull",
                token: token
            })
        } else {
            res.json({
                message: "User not found"
            })
        }

    } catch(error) {
        console.log(error)
        res.json(error)
    }

}

const resource = async (req, res)=>{
    const authorizationHeader = req.headers['authorization']
    const responseToken = authorizationHeader.split(" ")[1]

    try {
        const userInfo = jwt.verify(responseToken, "secret")

        if (userInfo.admin) {
            res.json({
                message: "Allowed Access to Endpoint"
            })
        } else {
            res.status(401).json({
                message: "Access to resource is not allowed. You are not an admin"
            })
        }


    } catch (error) {
        res.json(error)
    }

}


module.exports = {
  getHomePath,
  getAllUsers,
  createUser,
  loginUser,
  resource
};
