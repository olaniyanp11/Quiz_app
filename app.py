
from flask import Flask, url_for, render_template, redirect, request,flash, session
import requests
import html
from datetime import timedelta, datetime
import random
import urllib.parse
app = Flask(__name__)
import requests
import os
import json

app.secret_key ='3h*6j@0qP8!z5+*^bs9310-1'



@app.route("/")
def index():
    return render_template("index.html")


@app.route("/sort", methods=['POST'])
def sort():
    dict_data = request.form
    encoded_data = urllib.parse.urlencode(dict_data)
    return redirect (url_for('newexam', encoded_data=encoded_data))
# starts a new exam


@app.route("/newexam/<encoded_data>")
def newexam(encoded_data):
    dict_data = urllib.parse.parse_qs(encoded_data)
    dict_data["type"] = "multiple"
    try:
        response = requests.get("https://opentdb.com/api.php", params=dict_data)
        response.raise_for_status()
    except Exception:
        return render_template("error.html")
    data = response.json()
    name = dict_data["name"]
    name = name[0]
    question_bank = data["results"]
    for i in range(len(question_bank)):
        category = question_bank[i]["category"]
        type = question_bank[i]["type"]
        difficulty = question_bank[i]["difficulty"]
        session['username'] = name
        session['loggedin'] = True 
        app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=10)
    # putting the javascript in a file named "users"
    with open(name, 'w') as f:
        f.write(json.dumps(question_bank))
    return render_template("start.html",category=category,type=type,difficulty=difficulty,name=name)


#  route to start new exam   
@app.route("/startexam,/<name>")
def startexam(name):
    try:
        with open(name, 'r') as f:
            data = f.read() 
            data = json.loads(data)
        if data == []:
            flash('<h1>insufficient question</h1>')
            return render_template("index.html")
        else:
            return render_template('exam.html', questions=data, session=session,name=name)
    except FileNotFoundError:
            return render_template("index.html")
@app.route('/endsession', methods=['POST'])
def endsession():
    session.clear()
    return redirect(url_for('index'), code=302)


if __name__ == "__man__":
    app.run(debug=True)