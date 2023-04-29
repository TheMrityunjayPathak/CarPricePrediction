# CarPricePrediction

**Car Price Prediction using Linear Regression🚗**

Hello Everyone, 👋 

Here is My Regression Project based on Predicting Price of Car using Linear Regression.

- **Dataset**

I used Honda Used Car Selling Dataset which is My own Dataset uploaded on Kaggle.

**Link of the Dataset:** https://www.kaggle.com/datasets/themrityunjaypathak/honda-car-selling

- **Steps involved in the Project**

1️⃣ **Data Cleaning**

Data Cleaning involves cleaning Different Columns of Dataset like Year, kms Driven, Fuel Type, Suspension, Car Model, Price and removing all the Anomalies of the Dataset.

- Fuel Type, Suspension and Car Model has extra whitespaces which is removed by str.strip() Methods.

- Removing kms Suffix from kms Driven Column by using str.split() Method and converting it into Integer.

- Converting Price Column from 6.45 Lakh to 645000 and convering it into Integer by using a Custom Made Function.

- From Car Model Column picking up First 3 Words and removing the rest of the Words for better Accuracy of Model.

2️⃣ **Data Visualization**

Data Visualization involves visualizing Different Columns of Dataset like Year, kms Driven, Fuel Type, Suspension, Car Model, Price and finding Relationship among them.

- Visualizing Year with Price by using Swarm Plot and concluded that Old Cars has less Price as Compared to New Cars and Number of Old Cars on sale is also lesser than New cars. 

- Visualizing kms Driven with Price by using Relation Plot.

- Visualizing Car Model with Price by using Relation Plot and Suspension as Hue Parameter.

3️⃣ **Dummy Variable**

Dummy Variable Step inovolves converting Text Data into Numerical Data by using pd.get_dummies() Method for Model Traning as our Model only works on Numerical Data.Fuel Type, Suspension, Car Model are Text Columns which has to be converted into Numerical Columns by usind Dummy Variable Concept.

- We first Create Dummy Variable Column based on the Text Column.

- Then we change it into a DataFrame.

- After that we will Merge the Dummies DataFrame and our Orignal DataFrame.

- Finally we will drop the Text Column from our Dataset.

4️⃣ **Outlier Removal**

After Describing the Dataset I noticed that In our kms Driven Column, 75% of Cars has driven 85000 kms and our Maximum Value in kms Driven is 11 Lakh kms which is an Outlier and similarly In our Price Column, 75% of Cars has Price 7 Lakh and our Maximum Price is 26 Lakh which is an Outlier and we have to remove them.

5️⃣ **Model Building**

I used Linear Regression for this Problem as here we have to Predict the Price of Car based on Certain Features.

- Firstly I have definied Dependent and Independent Variables for our Traning and Testing.

- I have splitted data into Traning and Testing by using Train Test Split.

- Then I fit the Model with X_train and y_train and checked the Score.

- After that I used KFold Cross Validation for Measuring Accuracy of our Model.

- So I cheked Cross_Val_Score of our Model for Measuring the Best Score of Model and then I have taken Mean of All that Scores.

- And Finally I predicted the Result from our Trained Model.

📌 **Link to Notebook:** https://www.kaggle.com/code/themrityunjaypathak/car-price-prediction-using-linear-regression
