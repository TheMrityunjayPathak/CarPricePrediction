**Car Price Prediction using Linear Regression**

Hello Everyone, 👋 

Here is My Regression Project based on Predicting Price of Car using Linear Regression.

------------------------------------

🔸 **Dataset**

I used Honda Used Car Selling Dataset which is My own Dataset uploaded on Kaggle.

📍 **Link to the Dataset :** [Honda Used Car Selling](https://www.kaggle.com/datasets/themrityunjaypathak/honda-car-selling)

-------------------------------------

🌐 **Setting up the Enviroment**

Jupyter Notebook is required for this project and you can install and set it up in the terminal.

> Install the Notebook - `pip install notebook`

> Run the Notebook - `jupyter notebook`

------------------------------------------

🗃️ **Libraries required for the Project**

🔸 **NumPy**

> Go to Terminal and run this code - `pip install numpy`

> Go to Jupyter Notebook and run this code from a cell - `!pip install numpy`

🔸 **Pandas**

> Go to Terminal and run this code - `pip install pandas`

> Go to Jupyter Notebook and run this code from a cell - `!pip install pandas`

🔸 **Matplotlib**

> Go to Terminal and run this code - `pip install matplotlib`

> Go to Jupyter Notebook and run this code from a cell - `!pip install matplotlib`

🔸 **Seaborn**

> Go to Terminal and run this code - `pip install seaborn`

> Go to Jupyter Notebook and run this code from a cell - `!pip install seaborn`

🔸 **Sklearn**

> Go to Terminal and run this code - `pip install sklearn`

> Go to Jupyter Notebook and run this code from a cell - `!pip install sklearn`

-------------------------------------------

## Getting Started

- Clone the repository to your local machine using the following command :
```
git clone https://github.com/TheMrityunjayPathak/CarPricePrediction.git
```
--------------------------------------------

📝 **Steps involved in the Project**

1️⃣ **Data Cleaning**

Data Cleaning involves cleaning Different Columns of Dataset like Year, kms Driven, Fuel Type, Suspension, Car Model, Price and removing all the Anomalies of the Dataset.

- Fuel Type, Suspension and Car Model has extra whitespaces which is removed by str.strip() Methods.

- Removing kms Suffix from kms Driven Column by using str.split() Method and converting it into Integer.

- Converting Price Column from 6.45 Lakh to 645000 and convering it into Integer by using a Custom Made Function.

- From Car Model Column picking up First 3 Words and removing the rest of the Words for better Accuracy of Model.

2️⃣ **Data Visualization**

Data Visualization involves visualizing Different Columns of Dataset like Year, kms Driven, Fuel Type, Suspension, Car Model, Price and finding Relationship among them.

- Visualizing Year with Price by using sns.swarmplot() and concluded that Old Cars has less Price as Compared to New Cars and Number of Old Cars on sale is also lesser than New cars.

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/5e23ec76-ebe0-4f42-9d72-24b881eceeff)

- Visualizing kms Driven with Price by using sns.relplot().

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/3d7c4b1f-a2b3-47c7-8e0d-86c49aa80313)

- Visualizing Car Model with Price by using sns.relplot() and Suspension as Hue Parameter.

![download](https://github.com/TheMrityunjayPathak/CarPricePrediction/assets/123563634/c5faa6d5-46ed-4995-82fe-ec042beca0e4)

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

--------------------------------

📍 **Link to the Notebook :** [Car Price Prediction using Linear Regression](https://www.kaggle.com/code/themrityunjaypathak/car-price-prediction-using-linear-regression)
