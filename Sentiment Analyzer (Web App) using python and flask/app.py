from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = {}
    if request.method == "POST":
        txt = request.form["text"]
        blob = TextBlob(txt)
        
        # Keep full precision instead of rounding too early
        pol = blob.sentiment.polarity
        sub = blob.sentiment.subjectivity

        # Adjust threshold to be more sensitive
        if pol >= 0.1:
            sent = "Positive"
        elif pol <= -0.1:
            sent = "Negative"
        else:
            sent = "Neutral"

        result = {
            "text": txt,
            "polarity": round(pol, 3),
            "subjectivity": round(sub, 3),
            "sentiment": sent
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
