import numbers
from unicodedata import numeric
from flask import Flask, render_template, request, flash

app: Flask = Flask(__name__)
app.secret_key = "Bigman=1234"

@app.route("/")
def index() -> str:
    flash("What's your name?")
    return render_template("index.html")

@app.route("/age", methods=["POST", "GET"])
def age() -> str:    
    flash("Hi " + str(request.form['name_input']) + ". Please enter your year of birth")
    return render_template("age.html")  

@app.route("/thanks", methods=["POST", "GET"])
def thanks() -> str:
    agevalue: int= 2022 - int(request.form['num1_input'])
    flash("You were born in the year " +  str(request.form['num1_input']) + " and your are " + str(agevalue) + "yrs old. THANK YOU!")
    return render_template("thanks.html")