from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def Hello():
    return render_template("index.html", greetings="Hello Word !")

if __name__=="__main__":
    app.run()