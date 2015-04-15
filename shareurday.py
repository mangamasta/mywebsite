from flask import Flask, render_template, url_for, request, redirect, flash, session
from RandomWord import randword
from WordChecker import word_check
from sql_Database import sql_lite,readData
from read_db import readDataFirst
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

@app.route('/')
def begin():
    return render_template("shareurday.html")

if __name__ == "__main__":
    	app.run(debug=True)
