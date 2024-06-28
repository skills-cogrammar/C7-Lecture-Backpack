const app = require("./src/app");

const PORT = process.env.PORT || 8080;

console.log(process.env.MESSAGE)

app.set("port", PORT);
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});