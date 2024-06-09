const { Book } = require("../models/books");

const getHomeController = (req, res) => {
  res.json({
    message: "I have successfully used a custom hook!!",
  });
};

//CRUD
//Create
const createBook = async (req, res) => {
  const { title, author, price, image } = req.body;
  try {
    const createdBook = await Book.create({
      title,
      author,
      price,
      image,
    });

    res.status(201).json({
      message: "Success",
      book: createdBook,
    });
  } catch (error) {
    res.status(400).json({
      message: "Error",
      error,
    });
  }
};
//Read
const getAllBooks = async (req, res) => {
  try {
    const books = await Book.find(); //Finds all books (Returns a list of books)

    res.json({
      message: "Success",
      books: books,
    });
  } catch (error) {
    res.status(400).json({
      message: "Error",
      error,
    });
  }
};
//Update
const updateBook = async (req, res) => {
  const { id } = req.params;
  const { title, author, image, price } = req.body;
  try {
    const updatedBook = await Book.findByIdAndUpdate(id, {
      title: title,
      author: author,
      image: image,
      price: price,
    });

    res.json(
        {
            message: "Success",
            updatedBook
        }
    )
  } catch (error) {
    res.json({
      message: "Error",
      error,
    });
  }
};
//Delete
const deleteBook = async (req, res)=>{
    const { id } = req.params

    try {

        const deletedBook = await Book.findByIdAndDelete(id)

        res.json({
            message: "Success",
            book: deletedBook
        })

    } catch (error) {
        res.json({
            message: "Error",
            error
        })
    }
}

module.exports = {
  getHomeController,
  getAllBooks,
  createBook,
  updateBook,
  deleteBook
};
