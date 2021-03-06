# -*- coding: utf-8 -*-
"""Medical Insurance Cost Prediction_ML_.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IHKVtN6A9oq_DO0YTQCoYuwaZ2-hVisj
"""

from google.colab import drive
drive.mount('/content/drive')

"""* Importing the Dependencies/Libraries"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

"""*Here we are building a Automatic Predictor for Insurance Company, that will help the company to predict what is the 
Medical Insurance Cost of a person will be depending on the data given.
This sample dataset summarizes 1338 persons with 7 variables. (6 independent features and 1 dependent feature)*

*Will import all required libraries and load the data to perform data analysis operation like finding missing values, statistical measures, distribution of 
different values, etc. Then will import some categorical features into numerical value, after that will split data into features & target and in training and 
testing data too. 
Once we are done with all these process, will train and test our model with the help of Regression model. 
This way we will generate predictive model that will predict Medical insurance cost of a person by giving some input features.*
"""

# loading the data from csv file to a Pandas DataFrame
insurance_dataset = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/ML Project - Car Selling Price/insurance.csv')

# first 5 rows of the dataframe
insurance_dataset.head()

# number of rows and columns
insurance_dataset.shape

# getting some informations about the dataset
insurance_dataset.info()

"""**-Categorical Features**:It do not contain any numeric value.
- **Sex**       (Male/Female)
- **Smoker**    (Yes/No)
- **Region**    (Northwest/Northeast/Southeast/Southwest)
"""

# checking for missing values
insurance_dataset.isnull().sum()

"""**Note :** * We dont have any missing values in this dataset.*

* Data Analysis
"""

# statistical Measures of the dataset
insurance_dataset.describe()

# distribution of age value
sns.set()
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['age'])
plt.title('Age Distribution')
plt.show()

"""**-Note :** *The maximum no.of people are from 20 to 23-24 years age group.*"""

# Gender column
plt.figure(figsize=(6,6))
sns.countplot(x='sex', data=insurance_dataset)
plt.title('Sex Distribution')
plt.show()

insurance_dataset['sex'].value_counts()

"""**-Note :** *There is almost equal distribution for both the gender i.e male and female.*"""

# bmi distribution
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['bmi'])
plt.title('BMI Distribution')
plt.show()

"""Normal BMI Range --> 18.5 to 24.9"""

# children column
plt.figure(figsize=(6,6))
sns.countplot(x='children', data=insurance_dataset)
plt.title('Children')
plt.show()

insurance_dataset['children'].value_counts()

"""**-Note :** *There is a large no.of people who doesnt have children, which is almost leading the count to 580. And most of the people are having one child as compared to the other children count ( 2 or more childrens).*"""

# smoker column
plt.figure(figsize=(6,6))
sns.countplot(x='smoker', data=insurance_dataset)
plt.title('smoker')
plt.show()

insurance_dataset['smoker'].value_counts()

"""**-Note :** *Here we are having large no.of non-smoker people as compared to smoker.*"""

# region column
plt.figure(figsize=(6,6))
sns.countplot(x='region', data=insurance_dataset)
plt.title('region')
plt.show()

insurance_dataset['region'].value_counts()

"""**- Note :** *The data is almost simillar for all the different rigions, but southeast rigion is having litle kind of more.*"""

# distribution of charges value
plt.figure(figsize=(6,6))
sns.distplot(insurance_dataset['charges'])
plt.title('Charges Distribution')
plt.show()

"""**-Note :** *Most of the data is distributed in 10000  and very less no.od data has been distributed in 30 to 40000 .*

* Data Pre-Processing

Encoding the categorical features
"""

# encoding sex column
insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

3 # encoding 'smoker' column
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

"""Splitting the Features and Target"""

X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']

# features
print(X)

# target
print(Y)

"""* Splitting the data into Training data & Testing Data"""

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

print(X.shape, X_train.shape, X_test.shape)

"""**-Note :** *so here, 80% of data goes under training i.e (1070, 6) and 20% for testing i.e (268, 6).*

* Model Training

Linear Regression
"""

# loading the Linear Regression model
regressor = LinearRegression()

regressor.fit(X_train, Y_train)

"""**-Note :** *It will plot the line for datapoints.*

* Model Evaluation
"""

# prediction on training data
training_data_prediction =regressor.predict(X_train)

# R squared value
r2_train = metrics.r2_score(Y_train, training_data_prediction)
print('R squared vale : ', r2_train)

# prediction on test data
test_data_prediction =regressor.predict(X_test)

# R squared value
r2_test = metrics.r2_score(Y_test, test_data_prediction)
print('R squared vale : ', r2_test)

"""**-Note :** *For the best model, the training data value and testing data value needs to be almost equal to each other. SO here, in this case it is almost fullfilling this condition. Hence we dont have any over fitting issue in this case.*

* Building a Predictive System
"""

input_data = (31,1,25.74,0,1,0)

# changing input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the array
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = regressor.predict(input_data_reshaped)
print(prediction)

print('The insurance cost is USD ', prediction[0])