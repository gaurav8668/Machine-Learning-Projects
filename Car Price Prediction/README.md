<h2><b>The Project is Car Price Prediction, which predicts the price of a car. This is a Regression Problem.</b></h2>

<h1><b> Dataset <b></h1>
  Dataset is taken from kaggle: https://www.kaggle.com/nehalbirla/vehicle-dataset-from-cardekho
 
<h1> <b> About the Dataset </b> </h1>
  <ul>
    <li> Dataset has 9 columns. </li>
    <li> Car_Name, Year, Selling_Price, Present_Price, Kms_Driven, Fuel_Type, Seller_Type, Transmission, Owner. </li>
    <li> Present_Price is the dependent variable, and rest are independent variable. </li>
    <li> Shape of Dataset: (301, 9) </li>
   </ul>
 
<h1><b> Data Preprocessing </b></h1>
  <ul>
    <li> There are no null values in data. </li>
    <li> Converted Year columns to datetime. </li>
    <li> Categorical features like  Fuel_Type, Seller_Type, Transmission are handled by One-Hot Encoding. </li>
   </ul>

<h1><b> Hyper Parameter Tunning </b></h1>
    <ul>
      <li> RadomizedSearchCV</li>
    </ul>
  
<h1> <b> Mode Creattion </h1>
   <ul>
    <li> Random Forest Model is Used over here. </li>
    <li> The conclusion were made using rmse, mse, mae, r2score. </li>
   </ul>

<h1> Screenshot of the app </h1>
<img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/Car%20Price%20Prediction/screenshots_app/x.png">
<img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/Car%20Price%20Prediction/screenshots_app/x1.png">
  
 
