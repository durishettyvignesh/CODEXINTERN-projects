from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        txt = request.form["text"]
        blob = TextBlob(txt)
        pol = round(blob.sentiment.polarity, 2)
        sub = round(blob.sentiment.subjectivity, 2)

        if pol > 0:
            sent = "Positive"
        elif pol < 0:
            sent = "Negative"
        else:
            sent = "Neutral"

        result = {
            "text": txt,
            "polarity": pol,
            "subjectivity": sub,
            "sentiment": sent
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
