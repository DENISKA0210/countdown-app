from flask import Flask
from datetime import datetime, timedelta

app = Flask(__name__)

def days_until_saturday():
    today = datetime.today()
    saturday = today + timedelta((5 - today.weekday()) % 7)
    return (saturday - today).days

@app.route("/")
def home():
    return f"<h1>Днів до суботи: {days_until_saturday()}</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)