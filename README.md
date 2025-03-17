## Car Price Prediction

Hello Everyone,

Here is my regression project based on predicting the price of used cars using Linear Regression.

## Dataset

I used Honda Used Car Selling Dataset which is one of my own dataset uploaded on Kaggle.

**Link to the Dataset :** [Car Price Dataset](https://www.kaggle.com/datasets/themrityunjaypathak/honda-car-selling)

## Problem Statement

- To develop a Machine Learning Model that can accurately predict the prices of used cars based on various features and attributes.
  
- The predicted prices will assist both buyers and sellers in making informed decisions, ensuring fair transactions in the used car market.

## Streamlit Web App

- For my project, I have created a Streamlit Web App for predicting the prices of cars in more interactive and user friendly way.

- This web app allows you to predict the prices of the cars by just selecting some of its features and fill in some details.

- These all are the features you need to select or enter before pressing the predict button :

  - **Year** : Select the manufacturing year of the car.
    
  - **kms Driven** : Enter the total distance covered by the car.
    
  - **Fuel Type** : Choose the fuel type of the car.
    
  - **Suspension** : Pick the type of suspension.
    
  - **Car Model** : Select your car model from the available options.

- After selecting all these features, Just hit the '**Predict**' Button.

- This web app also has multiple error handling mechanisms to gracefully manage unexpected situations.

- I have named it AutoValuate.

**Link to the Web App :** [Car Price Prediction App](https://car-price-prediction-using-lr.streamlit.app/)

<a href="https://car-price-prediction-using-lr.streamlit.app/"><img src="https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/9c4ed16e-6741-48db-88ed-778c212ac380"/></a>

## Table of Contents

- [Setting up the Enviroment](#setting-up-the-enviroment)
- [Libraries required for the Project](#libraries-required-for-the-project)
- [Getting started with Repository](#getting-started)
- [Steps involved in the Project](#steps-involved-in-the-project)
- [Conclusion](#conclusion)

## Setting up the Enviroment

Jupyter Notebook is required for this project and you can install and set it up in the terminal.

- Install the Notebook
```
pip install notebook
```

- Run the Notebook
```
jupyter notebook
```

## Libraries required for the Project

**NumPy**

- Go to the terminal and run this code
```
pip install numpy
```

**Pandas**

- Go to the terminal and run this code
```
pip install pandas
```

**Matplotlib**

- Go to the terminal and run this code
```
pip install matplotlib
```

**Seaborn**

- Go to the terminal and run this code
```
pip install seaborn
```

**Sklearn**

- Go to the terminal and run this code
```
pip install scikit-learn
```

## Getting Started

- Clone this repository to your local machine by using the following command :
```
git clone https://github.com/TheMrityunjayPathak/CarPricePrediction.git
```

## Steps involved in the Project

**Data Cleaning**

- Fuel Type, Suspension and Car Model has extra whitespaces which gets removed by str.strip() method.

- Removed 'kms' suffix from Kms Driven column by using str.split() method and keeping only numeric part of the column.

- After that I converted Kms Driven column to 'int' DataType.

- Modified the Price column from 6.45 Lakh to 645000 and converted it into integer by using a custom made function.

- From Car Model column I kept only the first 3 words of car name and removed the rest.

**Data Visualization**

- Visualizing year with price column by using sns.swarmplot().

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/5e23ec76-ebe0-4f42-9d72-24b881eceeff)

- Visualizing kms_driven with price column by using sns.relplot().

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/3d7c4b1f-a2b3-47c7-8e0d-86c49aa80313)

- Visualizing car_model with price column by using sns.relplot() and suspension as 'hue' parameter.

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/c5faa6d5-46ed-4995-82fe-ec042beca0e4)

**Dummy Variable**

- I first created dummy variables based on the categorical columns.

- Then I transformed them into a DataFrame.

- After that I merged the dummies DataFrame and the orignal DataFrame.

- Finally I dropped the categorical columns from the dataset.

**Outlier Removal**

- First I used df.describe() method to get a summary of all numerical columns.

- Then I noticed that in kms_driven column, 75% of cars has travelled 85000 kms and the maximum value in kms_driven is 11 Lakh kms which is an outlier.
  
- And similarly, In price column, 75% of cars has price of 7 Lakh and the maximum car price is 26 Lakh which is an outlier.

**Model Building**

- I started by defining dependent and independent variables (X, y).

- Then I split the data into traning and testing set by using train_test_split.

- Then I fit the data on linear regression and checked the score.

- After that I used k-fold_cross_validation for further testing the robustness of the model.

- So I cheked mean cross_val_score of the model to further evaluate its prediction accuracy.

- And, finally I predicted the results from the trained model.

## Conclusion

- Trained a highly accurate Linear Regression model using various features and attributes to predict used car prices.

- Achieving an average prediction accuracy of 82%.

- Further model showcased its robustness by undergoing rigorous k-fold cross-validation, resulting in a mean cross-val-score of 83%.

- Lastly, I created a web application by using Streamlit.

<div align='left'>
  
**[`^        Scroll to Top       ^`](#car-price-prediction)**

</div>
