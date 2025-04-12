from flask import Flask, render_template

app = Flask(__name__)

app.config['SERVER_NAME'] = 'localhost:5001'
@app.route('/')
def home():
    return render_template('dashboard.html')  # template where Tableau is embedded

if __name__ == '__main__':
    app.run(debug=True)