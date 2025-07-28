#### **Matrix tool, Sentiment Analyzer \& House Price Tool - Python Projects**

--------------------------------------------------------



This repository contains 3 Python-based projects built for data analysis, machine learning, and basic NLP. 

Each tool uses simple logic, minimal dependencies, and is written in a clean, beginner-friendly format.





##### 1\.  House Price Prediction

--------------------------------------------------------



&nbsp;   Description:

&nbsp;   ------------

&nbsp;   A machine learning tool that predicts house prices using a linear regression model 

&nbsp;   trained on the Kaggle "House Prices" dataset. It uses features like quality, area, 

&nbsp;   year built, etc.





&nbsp;   What It Does:

&nbsp;   -------------

&nbsp;   - Loads CSV file with house data.

&nbsp;   - Cleans and encodes the dataset.

&nbsp;   - Trains a linear regression model.

&nbsp;   - Prints RMSE, R² score, and a sample prediction.





&nbsp;   How To Run:

&nbsp;   -----------

&nbsp;   1. Download `train.csv` from Kaggle: 

&nbsp;      https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques



&nbsp;   2. Place it next to the `house\_price\_model.py` file.



&nbsp;   3. Run using:

&nbsp;      python house\_price\_model.py





&nbsp;   Libraries Used:

&nbsp;   ---------------

&nbsp;   - pandas

&nbsp;   - numpy

&nbsp;   - scikit-learn









##### 2\.  Matrix Operations Tool

--------------------------------------------------------



&nbsp;   Description:

&nbsp;   ------------

&nbsp;   A terminal-based interactive tool that allows users to input two matrices and perform 

&nbsp;   basic operations like addition, subtraction, multiplication, transpose, and determinant 

&nbsp;   calculation.





&nbsp;   What It Does:

&nbsp;   -------------

&nbsp;   - Accepts user input for two matrices.

&nbsp;   - Performs supported operations if dimensions allow.

&nbsp;   - Shows all results clearly.





&nbsp;   How To Run:

&nbsp;   -----------

&nbsp;   1. Run:

&nbsp;      python matrix\_tool.py



&nbsp;   2. Enter row and column sizes, then matrix values.





&nbsp;   Libraries Used:

&nbsp;   ---------------

&nbsp;   - numpy







##### 

##### 3\.  Flask Sentiment Analysis Web App

--------------------------------------------------------



&nbsp;   Description:

&nbsp;   ------------

&nbsp;   A simple web application built using Flask and TextBlob that performs sentiment 

&nbsp;   analysis on user input text.





&nbsp;   What It Does:

&nbsp;   -------------

&nbsp;   - Takes text input via HTML form.

&nbsp;   - Uses TextBlob to analyze sentiment polarity and subjectivity.

&nbsp;   - Displays whether the text is Positive, Negative, or Neutral.





&nbsp;   How To Run:

&nbsp;   -----------

&nbsp;   1. Install required libraries:

&nbsp;      pip install flask textblob

&nbsp;      python -m textblob.download\_corpora



&nbsp;   2. Run:

&nbsp;      python app.py



&nbsp;   3. Open browser and go to:

&nbsp;      http://127.0.0.1:5000/





&nbsp;   Libraries Used:

&nbsp;   ---------------

&nbsp;   - flask

&nbsp;   - textblob









Author:

--------------------------------------------------------

&nbsp;   Vignesh Durishetty

