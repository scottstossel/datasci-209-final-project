import altair as alt
import pandas as pd
import json
from flask import Flask, render_template

app = Flask(__name__)

app.config['SERVER_NAME'] = 'localhost:5004'

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/direct-flights')
def direct_flights():
    return render_template('direct-flights.html')
@app.route('/currency')
def currency():
    return render_template('currency_dynamic.html')
@app.route('/tourism-overview')
def tourism_overview():
    return render_template('tourism_overview.html')
@app.route("/contact")
def contact():
    return render_template("contact.html")
    
if __name__ == '__main__':
    app.run(debug=True)