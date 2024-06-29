const authModel = require("../models/auth.model");
const jwt = require("jsonwebtoken");
const JWT_SECRET = process.env.JWT_SECRET;

/*
    This controller contains all of the logic 
    that is required to work with the database.

    The problem with this approach is that the function 
    are not easy to test since the each of the function 
    do not return values.

    The other prbolem is that our controller is tightly coupled with the MongoDB
    database, if we wanted to change databases, we would need to rewrite all of the code
    in the controller, and if we decide that we want to go back to mongodb 
    we would need to rewrite again.
*/


async function createUser(req, res){
    const { email, password } = req.body;    

    try{
        const user = await authModel.create({ email, password });
        console.log(user)
        res.status(201).json(user);
    } catch(err){
        res.status(400).json(err);    
    }
}

async function authenticateUser(req, res, next){
    const {email, password} = req.body;

    const user = await authModel.findOne({email}).select('+password');

    if (!user){
        const error = new Error("User not Found")
        error.status = 403
        return next(error);
    }



    try{
        const user = await authModel.findOne({email}).select('+password');

        if (!user){
            res.status(400).json({error: "User not found"});
        }

        user.comparePassword(password, (err, isMatch) => {
            if (err) throw err;

            if (isMatch){
                const payload = {
                    id: user._id,
                    role: user.role
                }

                const token = jwt.sign(payload, JWT_SECRET, {expiresIn: "7d"});

                res.status(200).json({message: "User authenticated", token: token});
            } else{
                res.status(400).json({message: "Invalid credentials"})
            }
        });
    } catch(err){
        res.status(400).json(err);    
    }
}

module.exports = {
    createUser,
    authenticateUser
}