const helloController = (req, res)=>{
    res.json({
        message: "Hello World"
    })
}


module.exports = {
    helloController
}