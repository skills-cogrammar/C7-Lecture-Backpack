const express = require("express");
const jwt = require("jsonwebtoken");
const app = express();

app.use(express.json());

app.get("/", (req, res) => {
  res.json({ message: "Hello World" });
});

app.post("/login", (req, res) => {
  const { username, password } = req.body;

  if (username === "Dan" && password === "1234") {
    
    const payload = {
      username: username,
      admin: true,
    };

    const token = jwt.sign(JSON.stringify(payload), "secret", {
      algorithm: "HS256",
    });

    res.json({
      message: "Request made successfully",
      token: token,
    });
  } else {
    //do something
    res.status(401).json({
      message: "Invalid Credentials",
    });
  }
});

app.get("/resource", (req, res) => {
  const authorizationToken = req.headers["authorization"];
  const token = authorizationToken.split(" ")[1];
  try {
    const response = jwt.verify(token, "secret");

    res.json({
      message: "Request was successfull",
      response: response.admin,
    });
  } catch (error) {
    res.json({
      message: "Invalid JWT Token",
    });
  }

  res.json({
    token: token,
  });
});

app.listen(8000, () => {
  console.log("Server is running on http://localhost:8000");
});
