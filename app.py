import os
from os import path
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route("/")  # Display main page with paginated list
@app.route("/calendar")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host=os.getenv("IP"),
            port=int(os.getenv("PORT")), debug=True)
