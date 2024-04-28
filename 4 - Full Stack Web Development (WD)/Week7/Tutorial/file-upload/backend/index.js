const http = require("http");
const fs = require("fs");
const formidable = require("formidable");
const path = require("path");

const PORT = 5000;
const UPLOADS_DIR = path.join(__dirname, "uploads");

// console.log(UPLOADS_DIR);

const server = http.createServer((req, res) => {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE");
  res.setHeader(
    "Access-Control-Allow-Headers",
    "Origin, X-Requested-With, Content-Type, Accept"
  );

  if (req.url == "/upload") {
    //Store the file to upload
    const form = new formidable.IncomingForm();
    form.uploadDir = UPLOADS_DIR;
    form.parse(req, (err, fields, files) => {
      const oldPath = files.file[0].filepath;
      const newPath = path.join(
        UPLOADS_DIR,
        `${files.file[0].newFilename}${files.file[0].originalFilename}`
      );

      fs.rename(oldPath, newPath, (err) => {
        if (err) {
          console.log(err);
        }

        console.log("Upload complete.");
        res.end();
      });
    });
  }
});

server.listen(PORT, function () {
  console.log(`Server is listening at port ${PORT}`);
});
