# Suicide-Analysis

This project predicts future suicide rates using data provided by a public sector.

This project uses Machine Learning Algorithm to predict the future annual suicides numbers.
We use pandas framework to clean the data to remove the noisy data.
The pandas data is converted to numpy and splitted into training and testing sets of 7:3

The data which is then feeded into a method provided by scikit-learn package to perform the Linear Regression.
Since the data is sub-classified into different categories, such as, age, gender, type of suicide, etc.
We took an iterative approach to make the model learn the patterns found.
