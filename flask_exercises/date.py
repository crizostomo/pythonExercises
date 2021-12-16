from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/date", methods = ["POST", "GET"])
def home():
    date = datetime.now()
    print(date)
    return date.strftime("%d/%m/%y")


if __name__ == "__main__":
    app.run()