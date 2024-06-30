// This middleware can be used to handle any errors that are thrown 
// this will be added to the app.js file as a global piece of middleware
// so that all error that are thrown can show proper messages
const errorHandler = (err, req, res, next) => {
    // The err header is reuqired since we will be passing an error 
    // in the next() call when we encounter bad input
    if (err) {
        res.status(err.status).json({
            message: err.message,
            source: "Error Middleware"
        })
    }
}

module.exports = errorHandler;