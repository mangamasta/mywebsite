from flask import Flask, render_template, url_for, request, redirect, flash, session
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
#---------------------------------------------------------------------
app = Flask(__name__)

@app.route('/')
def begin():
    return render_template("play.html")

app.config['SECRET_KEY'] = 'thisismysecretkeywhichyouwillneverguesshahahahahahahaha'
if __name__ == "__main__":
    	app.run(debug=True)