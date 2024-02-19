from flask import Flask
from datetime import datetime 

app = Flask(__name__)


@app.route("/")
def run():
    return 'Aditya Deshpande netid: amd9295'

@app.route("/time")
def showTime():
    return str(datetime.now())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8080"), debug=False)