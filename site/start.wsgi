import sys
import os

# Add the path to your Flask app directory
sys.path.insert(0, '/groups/global_tourism_insights/w209')

# Set the environment variable for Flask if needed
os.environ['FLASK_ENV'] = 'production'

# Import the Flask app
from app import app as application