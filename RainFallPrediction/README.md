# Rain-Prediction
<h3>The project is about rain fall prediction which predicts weather rain will come tomorrow or not. The data set is taken from kaggle.</h3>

# Dataset: <h2>https://www.kaggle.com/jsphyg/weather-dataset-rattle-package</h2>

# Tech Stack
* Front-End: HTML, CSS, Bootstrap
* Back-End: Flask
* IDE: Jupyter notebook, Pycharm

# How to run this app
* First create a virtual environment by using this command:
* conda create -n myenv python=3.6
* Activate the environment using the below command:
* conda activate myenv
* Then install all the packages by using the following command
* pip install -r requirements.txt
* Now for the final step. Run the app
* python app.py

# Some screenshots of the app
* Landing Page:
<img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/RainFallPrediction/ss1.png">
* About Rainy Brain:
<img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/RainFallPrediction/ss2.png">
* Predictor:
<img src="https://github.com/gaurav8668/Machine-Learning-Projects/blob/main/RainFallPrediction/ss3.png">


# Workflow

# Data Preprocessing: 
* Missing Values Handled by Random Sample imputation to maintain the variance
* Categorical Values like location, wind direction are handled by using Target guided encoding
* Outliers are handled using IQR and boxplot
* Feature Selection and was done but didnt perform well it can be seen in testing_notebook/Prediction.ipynb
* Feature Scaling didnt give a lot of difference it also can be seen in testing_notebook/RainPrediction1.ipynb
* Imbalanced Dataset was handled using SMOTE
# Model Creation:
* Different types of models were tried like catboost, random forest, logistic regression, xgboost, support vector machines, knn, naive bayes.
* Out of these catboost, random forest and support vector machines were top 3
* The conclusion were made using classification metrics. roc curve and auc score




