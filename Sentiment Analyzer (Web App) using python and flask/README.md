#### Sentiment Analyzer Web App

#### By **Vignesh Durishetty**

-----------------------------

This is a simple web app I made using Python and Flask. It takes text input from the user and tells whether the text is positive, negative, or neutral. It also shows two scores – polarity and subjectivity.

I used the TextBlob library for sentiment analysis and Flask to build the backend and display the results on a webpage.

-----------------------------

What I used and why

1. Python – the main language for this project  
2. Flask – for building the web app interface  
3. TextBlob – to do the sentiment analysis easily  
4. HTML – to create a form for user input and display results

-----------------------------

How I made it

1. First, I wrote a simple Flask app that has two routes: one for showing the input form and one for processing the result  
2. In the form, I allowed users to type any text  
3. On submission, the server reads the text and uses TextBlob to analyze it  
4. The result is shown back to the user, including the sentiment and two scores

-----------------------------

How it works (basic logic behind it)

1. TextBlob looks at the words and phrases in the sentence  
2. It calculates a polarity score from -1 (very negative) to +1 (very positive)  
3. It also gives a subjectivity score from 0 (very objective) to 1 (very subjective)  
4. Based on the polarity value:  
   - If polarity ≥ 0.1 → it's positive  
   - If polarity ≤ -0.1 → it's negative  
   - If polarity is between -0.1 and 0.1 → it's neutral  
5. These results are sent to the frontend and displayed nicely

-----------------------------

How to run it

1. Install the required libraries:  
   pip install Flask textblob  
   python -m textblob.download_corpora  

2. Run the app:  
   python app.py  

3. Open your browser and go to:  
   http://localhost:5000  

4. Type your text and submit to see the sentiment analysis result