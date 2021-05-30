<h2><b>The Project is Fligt Fare Prediction, which predicts the fare of a flight. This is a Regression Problem.</b></h2>

<h1><b> Dataset <b></h1>
  Dataset is taken from kaggle: https://www.kaggle.com/nikhilmittal/flight-fare-prediction-mh
  
<h1> <b> About the Dataset </b> </h1>
  <ul>
    <li>Dataset has 11 columns.</li>
    <li>Airline, Data_of_Journey, Source, Destination, Route, Dep_Time, Arrival_Time, Duration, Total_Stops, Addition_Info, Price.</li>
    <li>type of Price is int64 and rest are object.</li>
    <li> Shape of Dataset: (10683, 11) </li>
  </ul>
  
<h1><b> Data Preprocessing </b></h1>
  <ul>
  <li>There are no null values in the dataset.</li>
  <li>Convert Date_of_Journey, Arrival, Dep_Time, Duration into datetime column.</li>
  <li>Categorical Value are handles by Label Encoding, One-hot Encoding.</li>
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
  
<h1><b> How to Run this app </b></h1>
   <ul>
     <li>First create a virtual environment by using this command:</li>
     <li>conda create -n myenv python=3.7</li>
     <li>Activate the environment using the below command:</li>
     <li>conda activate myenv</li>
     <li>Then install all the packages by using the following command</li>
     <li>pip install -r requirements.txt</li>
     <li>Now for the final step. Run the app</li>
     <li>python app.py</li>
   </ul>
 
<h1> Screenshot of the app </h1>
  <img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/Flight-Fare-Prediction/ss_app.png">
  
