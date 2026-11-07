TITTLE --                     	Customer Churn Prediction 

ABOUT -- The purpose of this project is to build a machine learning  model that predicts whether customer will leave the company or not , based upon there demographic and service-related information.

PROBLEM STATEMENT -- Customer churn is a major challenge for businesses, as losing customers can negatively impact revenue and growth. This model can help businesses identify customers who are at risk of leaving and take proactive steps to improve customer retention.

DATASET -- This dataset is downloaded from kaggle , it have (1000 rows and 10 columns) . 

TECHNOLOGIES used -- Python , Pandas , Numpy , Seaborn , Matplotlib etc....

APPROACH--
we imported the dataset in CSV format , stored it in "df" object . Ran some info , isnull commands and got that in column name -> 'internet service ' we have 297 values missing....
since it is imp column for our model we decided to keep it and we removed the "Nan" with empty space for now...
next checked for any Duplicate values and it came 0 .
Now we checked for correaltions btw numerical columns and we got one (btw - monthly charge and Tenure)...

next we did some Data Visualizations for more insights--

next we will do - Feature Engineering ....
ENCODING --> we did Binary Encoding on two categorical columns (CHURN , GENDER ) , we did binary encoding because both columns have only 2 options..

next we are doing Feature Scaling ....
we are doing Standardiztion...+ saved this scaler in form of .pkl file.....
next to calculate accuracy score of models we made a function called - modelperformance.
we trained and transformed our model and getting the accuracy of - 85%...after getting aaccuracy score on Logistic regression algorithm , we know train new algorithm on the same data set to compare the aaccuracy score..
accuracy for KNEIGHBOURS came - 84%
accuracy for SVM came - 87%
accuracy for DECISION TREE CLASSIFIER -  85%
accuracy for RANDOM FOREST CLASSIFIER - 83%

in the very end we choose the model which gave the most accuracy percentage i.e - SVM..

Model is exported as model.pkl