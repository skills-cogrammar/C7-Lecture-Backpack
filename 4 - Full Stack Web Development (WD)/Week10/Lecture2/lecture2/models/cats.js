const mongoose = require('mongoose');

const catsSchema = mongoose.Schema({
  common_name: {
    type: String,
    required: true
  },

  scientific_name: {
    type: String,
    required: true
  }
});

module.exports = mongoose.model('Cats', catsSchema);