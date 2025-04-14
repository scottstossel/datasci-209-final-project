import altair as alt
import pandas as pd
import json
from flask import Flask, render_template

app = Flask(__name__)

app.config['SERVER_NAME'] = 'localhost:5007'

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/direct-flights')
def flights():
    return render_template('direct_flights.html')
@app.route('/currency')
def currency():
    return render_template('currency_dynamic.html')
@app.route('/tourism-overview')
def tourism():
    return render_template('tourism_overview.html')
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route('/about')
def about():
    return render_template('about.html')
    
if __name__ == '__main__':
    app.run(debug=True)