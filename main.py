from flask import Flask, redirect, url_for, render_template 
import random

app = Flask(__name__)

f = open("words.txt").read().splitlines()

words = []


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/home")
def home():
    words = []
    for i in range(75):
        words.append(random.choice(f))
    return render_template("home.html", content=words)

def check(word):
    pass

if __name__ == "__main__":
    app.run()