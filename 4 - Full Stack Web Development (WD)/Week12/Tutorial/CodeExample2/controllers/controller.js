const { User } = require("../models/Users");
const jwt = require("jsonwebtoken")

const getHomePath = (req, res) => {
  res.json({
    message: "Hello World",
  });
};

const updateUser = async (req, res) => {    
  const { username, password, admin } = req.body;
  const {id} = req.params
  try {
    const updatedUser = await User.findByIdAndUpdate(
      id, // Find by ID part of the query
      { // The data we want to update, will link the field names to the variables names we pass
        username,
        password,
        admin,
      },
      { new: true }
    );
    res.json({
      message: "User updated",
      data: {
        username: updatedUser.username,
        password: updatedUser.password,
        admin: updatedUser.admin,
      },
    });
  } catch (err) {
    console.log(err);
  }
}

// This function shows how we can use the data in the JWT to get information 
// About the user
const getUser = async (req, res) => {  
  try {
    const id = getJwtPayload(req).id    
    const user = await User.findById(id);
    res.json({
      message: "User fetched",
      data: {
        id: user._id,    
        username: user.username,
        password: user.password,
        admin: user.admin
      },
    });
  } catch (err) {
    console.log(err);
  }
};

const getJwtPayload = (req) => {
  const authorizationHeader = req.headers['authorization']

  try {
    const token = authorizationHeader.split(" ")[1]
    const userInfo = jwt.verify(token, "secret")

    if (userInfo){
      return userInfo
    }

    return null

  } catch (error) {
    throw new Error("Session Token Required")
  }
}



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
    console.log(username, password)

    try {
        const foundUser = await User.findOne({username: username, password: password})
        if ( foundUser ) {
            const payload = {
                admin: foundUser.admin,
                username: foundUser.username,
                id: foundUser._id // NEW CODE
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

//checking if user is an admin or not
const resource = async (req, res)=>{
    const authorizationHeader = req.headers['authorization']            

    try {        
        const responseToken = authorizationHeader.split(" ")[1]
        const userInfo = jwt.verify(responseToken, "secret")        

        if (userInfo.admin) {
            res.json({
                message: `${userInfo.username} has access to this endpoint`
            })
        } else {
            res.status(401).json({
                message: "Access to resource is not allowed. You are not an admin"
            })
        }


    } catch (error) {
        res.status(401).json("Session Token required")
    }

}


module.exports = {
  getHomePath,
  getAllUsers,
  createUser,
  loginUser,
  resource,
  getUser,
  updateUser
};
