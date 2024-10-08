const express = require('express')
const cors = require('cors')

const app = express()
app.use(cors())

app.get("", (req,res) => {
	res.status(200).json({
		"message": "This is a messaeg from out of space"
		"env": process.env.SECRET_VALUE
	})
})

app.set("PORT", 9000)
app.listen(9000, () => {
	console.log("something")
})
