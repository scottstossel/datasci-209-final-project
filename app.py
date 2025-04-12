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
    return render_template('currency.html')
if __name__ == '__main__':
    app.run(debug=True)