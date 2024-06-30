const app = require("./src/app");

const PORT = 8000;

app.set('port', PORT)

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`)
})