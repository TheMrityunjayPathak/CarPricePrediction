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

- fuel_type, suspension and car_model has extra whitespaces which is removed by str.strip() method.

- Removed kms suffix from kms_driven column by using str.split() method and keeping only numeric part of the column.

- After that we can convert kms_driven column to **'int'** DataType.

- Modifying price column from 6.45 Lakh to 645000 and convering it into integer by using a custom made function.

- From car_model column we will keep only first 3 words of car name and removing the rest.

**Data Visualization**

- Visualizing year with price by using sns.swarmplot()

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/5e23ec76-ebe0-4f42-9d72-24b881eceeff)

- Visualizing kms_driven with price by using sns.relplot()

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/3d7c4b1f-a2b3-47c7-8e0d-86c49aa80313)

- Visualizing car_model with price by using sns.relplot() and suspension as **'hue'** parameter

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/c5faa6d5-46ed-4995-82fe-ec042beca0e4)

**Dummy Variable**

- We first create dummy variable column based on the text column.

- Then we transform it into a DataFrame.

- After that we will merge the dummies DataFrame and our orignal DataFrame.

- Finally we will drop the text column from our dataset.

**Outlier Removal**

- After describing the dataset I noticed that in kms_driven column, 75% of cars has travelled 85000 kms and our maximum value in kms_driven is 11 Lakh kms which is an outlier.
  
- And similarly, In our price column, 75% of cars has price 7 Lakh and our maximum price is 26 Lakh which is an outlier.

**Model Building**

- Firstly I have definied dependent and independent variables for our traning and testing.

- I have splitted data into traning and testing set by using train_test_split.

- Then I fit the model with X_train and y_train and checked the score.

- After that I used k-fold cross-validation for measuring accuracy of our model.

- So I cheked the cross_val_score to get the best score of our model and then I have taken mean of all the scores.

- And, Finally I predicted the result from our trained model.

## Conclusion

- Developed a highly accurate Linear Regression Model using various features and attributes to predict used car prices, achieving an average prediction accuracy of 82%.

- Further model showcased its robustness by undergoing rigorous k-fold cross-validation, resulting in a mean cross-val score of 83%.

<div align='left'>
  
**[`^        Scroll to Top       ^`](#car-price-prediction)**

</div>
