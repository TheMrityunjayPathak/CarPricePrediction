## Car Price Prediction

Hello Everyone,

Here is My Regression Project based on Predicting Price of Car using Linear Regression.

## Dataset

I used Honda Used Car Selling Dataset which is one of my own Dataset uploaded on Kaggle.

**Link to the Dataset :** [Car Price Dataset](https://www.kaggle.com/datasets/themrityunjaypathak/honda-car-selling)

## Problem Statement

- To develop a Machine Learning Model that can accurately predict the prices of used cars based on various features and attributes.
  
- The predicted prices will assist both buyers and sellers in making informed decisions, ensuring fair transactions in the used car market.

## Streamlit Web App

- For my Car Price Prediction Project, I have created a Streamlit Web App for predicting the prices of cars in more interactive and user friendly way.

- This Web App allows you to predict the price of a car by just selecting some of its features and fill in some details.

- These all are the features you need to select or enter before Pressing the Predict Button :

  - **Year** : Select the manufacturing Year of the Car.
    
  - **kms Driven** : Input the Total Distance the Car has traveled.
    
  - **Fuel Type** : Choose the Fuel Type of the Car.
    
  - **Suspension** : Pick the Type of Suspension the Car has.
    
  - **Car Model** : Select Your Car Model from the available options.

- After selecting all these features, Just hit the '**Predict**' Button.

- This Web App also has multiple constraints in the Input Feilds.

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

**Pandas**

- Go to Terminal and run this Code
```
pip install pandas
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install pandas
```

**Matplotlib**

- Go to Terminal and run this Code
```
pip install matplotlib
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install matplotlib
```

**Seaborn**

- Go to Terminal and run this Code
```
pip install seaborn
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install seaborn
```

**Sklearn**

- Go to Terminal and run this Code
```
pip install scikit-learn
```

- Go to Jupyter Notebook and run this Code from a Cell
```
!pip install scikit-learn
```

## Getting Started

- Clone the repository to your local machine using the following command :
```
git clone https://github.com/TheMrityunjayPathak/CarPricePrediction.git
```

## Steps involved in the Project

**Data Cleaning**

- Fuel Type, Suspension and Car Model has extra whitespaces which is removed by str.strip() Method.

- Removing kms Suffix from kms Driven Column by using str.split() Method and keeping only Numeric Part of the String and removing kms Suffix.

- After that we can convert kms Driven Column to int DataType.

- Modifying Price Column from 6.45 Lakh to 645000 and convering it into Integer by using a Custom Made Function.

- From Car Model Column we will keep only First 3 Words of Cae Model and removing the rest of the Words for better Model Traning.

**Data Visualization**

- Visualizing Year with Price by using sns.swarmplot()

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/5e23ec76-ebe0-4f42-9d72-24b881eceeff)

- Visualizing kms Driven with Price by using sns.relplot()

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/3d7c4b1f-a2b3-47c7-8e0d-86c49aa80313)

- Visualizing Car Model with Price by using sns.relplot() and Suspension as Hue Parameter

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/c5faa6d5-46ed-4995-82fe-ec042beca0e4)

**Dummy Variable**

- We first Create Dummy Variable Column based on the Text Column.

- Then we change it into a DataFrame.

- After that we will Merge the Dummies DataFrame and our Orignal DataFrame.

- Finally we will drop the Text Column from our Dataset.

**Outlier Removal**

- After describing the Dataset I noticed that in our kms Driven Column, 75% of Cars has driven 85000 kms and our Maximum Value in kms Driven is 11 Lakh kms which is an Outlier.
  
- And Similarly In our Price Column, 75% of Cars has Price 7 Lakh and our Maximum Price is 26 Lakh which is an Outlier.

**Model Building**

- Firstly I have definied Dependent and Independent Variables for our Traning and Testing.

- I have splitted data into Traning and Testing Set by using Train Test Split.

- Then I fitted the Model with X_train and y_train and checked the Score.

- After that I used KFold Cross Validation for Measuring Accuracy of our Model.

- So I cheked Cross_Val_Score of our Model for Measuring the Best Score of Model and then I have taken Mean of All that Scores.

- And Finally I predicted the Result from our Trained Model.

## Conclusion

- Developed a highly accurate Linear Regression Model using various features and attributes to predict used car prices, achieving an average prediction accuracy of 82%.

- Further Model showcased its robustness by undergoing rigorous k-fold cross-validation, resulting in a mean cross-validation score of 83%.

<div align='right'>
  
**[`^        Scroll to Top       ^`](#car-price-prediction)**

</div>
