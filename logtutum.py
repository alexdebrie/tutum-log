from flask import Flask
from datetime import datetime 
import logging
import sys

app = Flask(__name__)
app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.INFO)

@app.route("/")
def main():
    app.logger.info("You just logged a request from Tutum!")
    return "Hello, Tutum!"

@app.route("/time")
def time():
    now = datetime.now()
    dt_string = now.strftime("%B %d, %Y")
    app.logger.info("Somebody visited at {}!".format(dt_string))
    return "Today is {}".format(dt_string)

if __name__ == "__main__":
    app.run()
