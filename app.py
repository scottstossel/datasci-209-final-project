import altair as alt
import pandas as pd
import json
from flask import Flask, render_template

app = Flask(__name__)

app.config['SERVER_NAME'] = 'localhost:5004'
@app.route('/')
def home():
    return render_template('index.html')  # template where Tableau is embedded
@app.route('/direct-flights')
def direct_flights():
    return render_template('direct-flights.html')
    
@app.route('/currency')
def currency():
    # Sample data
    df = pd.DataFrame({
        'Currency': ['USD', 'EUR', 'GBP', 'JPY', 'CAD', 'AUD'],
        'Tourists': [300, 280, 260, 200, 220, 210],
        'Country': ['USA', 'Europe', 'UK', 'Japan', 'Canada', 'Australia']
    })

    chart = alt.Chart(df).mark_circle(size=100).encode(
        x='Currency',
        y='Tourists',
        tooltip=['Country', 'Tourists']
    ).properties(
        width=600,
        height=400,
        title='Currency Strength vs Number of Tourists'
    )

    chart_json = chart.to_json()

    return render_template('currency_dynamic.html', chart_spec=chart_json)
if __name__ == '__main__':
    app.run(debug=True)