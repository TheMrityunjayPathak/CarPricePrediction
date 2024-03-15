#Importing Libraries
import streamlit as st
import pandas as pd
import sklearn
import pickle

#Reading CSV File
df = pd.read_csv("Cleaned_Car_Data.csv")

#Outlier Removal
df = df[df["Price"]<1000000]

df = df[df["kms Driven"]<150000]

#Loading ML Model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

#Setting Page Configuration
st.set_page_config(page_title="AutoValuate",page_icon="🚗",layout="centered")

st.markdown("<div style='background-color:#219C90; border-radius:50px; align-items:center; justify-content: center;'><h1 style='text-align:center; color:white;'>AutoValuate</h1></div>",unsafe_allow_html=True)

st.markdown("<h4 style='text-align:center; color:black;'>Find the Best Price for Your Car</h4>",unsafe_allow_html=True)

#Styling Streamlit Web App
col1, col2 = st.columns(2)

with col1:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.image("car.jpg",use_column_width=True)

with col2:
    car_model = st.selectbox(label="Select the Car Model",options=df["Car Model"].unique(),placeholder="Select the Model of Your Car",index=None)

    kms_driven = st.number_input(label="Enter the KMS Driven",placeholder="Enter the KMS Driven of Your Car",value=None,min_value=2000,max_value=140000,step=1000)

    col3, col4 = st.columns(2)

    with col3:
        fuel_type = st.radio(label="Select the Fuel Type",options=df["Fuel Type"].unique(),index=None)
    with col4:
        suspension_type = st.radio(label="Select the Suspension Type",options=df["Suspension"].unique(),index=None)

    year = st.slider(label="Select the Year",min_value=2000,max_value=2023,step=1)

    pred = st.button("Predict",use_container_width=True)

#Creating DataFrame
data = {'Year': [year], 'kms Driven': [kms_driven], 'Fuel Type': [fuel_type], 'Suspension': [suspension_type], 'Car Model': [car_model]}

df1 = pd.DataFrame(data)

#Dummies for Fuel Type
dummies1 = pd.get_dummies(df1["Fuel Type"],dtype = "int")

fuel_dummies = pd.DataFrame(dummies1)

df2 = pd.concat([df1,fuel_dummies],axis = "columns")

#Dummies for Suspension
dummies2 = pd.get_dummies(df2["Suspension"],dtype = "int")

suspension_dummies = pd.DataFrame(dummies2)

df3 = pd.concat([df2,suspension_dummies],axis = "columns")

#Dummies for Car Model
dummies3 = pd.get_dummies(df3["Car Model"],dtype = "int")

car_dummies = pd.DataFrame(dummies3)

df4 = pd.concat([df3,car_dummies],axis = "columns")

#Dropping Unwanted Column
df5 = df4.drop(["Fuel Type","Suspension","Car Model"],axis = "columns")

#Defining the Correct Order for Columns
model_features = ['Year', 'kms Driven', 'CNG', 'Diesel', 'Petrol', 'Automatic',
       'Manual', 'Honda Accord 2.4', 'Honda Accord VTi-L', 'Honda Amaze E',
       'Honda Amaze EX', 'Honda Amaze Exclusive', 'Honda Amaze S',
       'Honda Amaze SX', 'Honda Amaze V', 'Honda Amaze VX',
       'Honda Amaze i-DTEC', 'Honda BR-V i-DTEC', 'Honda BR-V i-VTEC',
       'Honda Brio 1.2', 'Honda Brio EX', 'Honda Brio S', 'Honda Brio V',
       'Honda Brio VX', 'Honda CR-V 2.0', 'Honda CR-V 2.0L', 'Honda CR-V 2.4',
       'Honda CR-V 2.4L', 'Honda CR-V Diesel', 'Honda CR-V Petrol',
       'Honda CR-V RVi', 'Honda City 1.3', 'Honda City 1.5',
       'Honda City Anniversary', 'Honda City Corporate', 'Honda City E',
       'Honda City EXi', 'Honda City GXi', 'Honda City S', 'Honda City SV',
       'Honda City V', 'Honda City VTEC', 'Honda City VX', 'Honda City ZX',
       'Honda City i', 'Honda City i-DTEC', 'Honda City i-VTEC',
       'Honda Civic 1.8', 'Honda Civic VX', 'Honda Civic ZX', 'Honda Jazz 1.2',
       'Honda Jazz 1.5', 'Honda Jazz Basic', 'Honda Jazz S',
       'Honda Jazz Select', 'Honda Jazz V', 'Honda Jazz VX', 'Honda Jazz X',
       'Honda Mobilio E', 'Honda Mobilio RS', 'Honda Mobilio S',
       'Honda Mobilio V', 'Honda WR-V Edge', 'Honda WR-V SV', 'Honda WR-V VX',
       'Honda WR-V i-DTEC', 'Honda WR-V i-VTEC']

#Adjusting the Features to match the Original DataFrame
for feature in model_features:
    if feature not in df5.columns:
        df5[feature] = 0

df5 = df5[model_features]

#Making Prediction by Trained ML Model
if pred:
    if any([car_model is None, kms_driven is None, fuel_type is None, suspension_type is None]):
        st.error("Please, Select all Inputs before Pressing Predict Button.",icon="📝")
    else:
        prediction = model.predict(df5)[0]
        if prediction < 0:
            st.error("Predicted Price is Below Zero, Please select Valid Inputs.", icon="⚠️")
        else:
            st.success(f"Predicted Price of Your Car is : ₹{prediction:,.0f}", icon="✅")
