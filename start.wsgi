import sys
import os

# Add the path to your Flask app directory
sys.path.insert(0, '/groups/global_tourism_insights/w209')
activate_this = '/groups/global_tourism_insights/w209/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Set the environment variable for Flask if needed
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application