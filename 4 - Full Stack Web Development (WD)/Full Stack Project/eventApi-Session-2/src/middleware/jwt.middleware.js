const jwt = require("jsonwebtoken")
const JWT_SECRET = process.env.JWT_SECRET;

/*
    Middleware intercepts the request that is being sent 
    from other pieces of middleware and can make changes to it.
    In this case, we are taking teh jwt token from the header and
    performing some operations based on whether the token is valid or not
*/


function verifyJwt(req, res, next){
    // Take the token from the authorization header
    const authHeader = req.headers.authorization;

    // If there is an auth header, check if it's valid
    if (authHeader){
        // Extract the token from the authHear,
        // The token would look like 'Bearer toknocihiodufghaosdifbasidufbasidufbasdfasdf'
        // We are splitting by the space so that we can only pass the token without the 
        // word 'Bearer '
        const token = authHeader.split(" ")[1];

        // Once we have the token, we can use the method from jsonwebtoken
        // to verify that the token is correct, 
        // the toekn that was passed will be decrypted using out SECRET and 
        // the internals will make sure that the token hasn't expired
        jwt.verify(token, JWT_SECRET, (err, user) => {            
            if (err) return res.sendStatus(403);

            // We are getting the payload from the JWT and naming 'user'
            // The 'user' is passed in the verify method
            // We as adding the user to the request header so that the next 
            // piece of middleware can access the information
            req.user = user;

            // The next method will tell express to go to the next piece of middleware
            next();
        });
    } else{
        res.sendStatus(401);
    }
}

// This function will be tightly coupled with the verifyJwt
// It depends on the user being authenticated already 
// and the user field being added to the req
function verifyAdmin(req, res, next){

    // Check if there is no user even though this i unlikely 
    // But we need to guard against the person calling the 
    // middleware putting things in the wrong place.
    if (!req.user){
        return res.sendStatus(403);
    }

    // Check if the role is admin, if it is
    // we can go to the next piece of middleware
    if (req.user.role == "admin"){
        next();    
    }
    else{
        // If the users role is not admin, we can rend them a forbidden warning 
        res.sendStatus(403);
    }
}

module.exports = {verifyJwt, verifyAdmin};