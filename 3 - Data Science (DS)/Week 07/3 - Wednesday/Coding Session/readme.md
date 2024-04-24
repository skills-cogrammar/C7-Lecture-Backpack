# Linear Regression Project

This repository contains code for a simple linear regression project.

## Files

### `linear_regression_training.py`

This file contains the code for training a linear regression model on the provided dataset (`salary_dataset.csv`). It includes procedures for data preprocessing, model training, and evaluation.

### `mean_square_error.py`

This file contains a custom implementation of the Mean Squared Error (MSE) metric for evaluating the performance of the trained model.

### `predict.py`

This file is used for making predictions using the trained linear regression model. It loads the model from the `salary_model.joblib` file and provides a function to predict salaries based on input features.

### `r_squared.py`

This file contains a custom implementation of the R-squared (R2) metric for evaluating the goodness-of-fit of the trained model.

### `salary_dataset.csv`

This CSV file contains the dataset used for training the linear regression model. It includes features such as years of experience and corresponding salaries.

### `salary_model.joblib`

This file stores the trained linear regression model in a serialized format using joblib.

## Usage

To train the linear regression model, run `linear_regression_training.py`. Make sure to have `salary_dataset.csv` in the same directory.

After training the model, you can use `predict.py` to make predictions on new data. Ensure that `salary_model.joblib` exists before running this script.

## Dependencies

- Python 3.x
- scikit-learn
- pandas
- numpy
- matplotlib

