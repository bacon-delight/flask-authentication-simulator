from flask import Flask
from flask_cors import CORS


# Initialise Application
app = Flask(__name__)

# Enable CORS
CORS(app)

# Import Configurations
import configs

# Enable Commands
with app.app_context():
	from commands import *

# Import Error Handlers
import errors

# Blueprint Imports
from apis.auth import auth

# Blueprint Registrations
app.register_blueprint(auth, url_prefix='/auth')

# Application Status Check
@app.route('/status', methods=['GET'])
def statusCheck():
	return make_response(
		'Site is Active',
		200,
		{'WWW-Authenticate': 'Basic Realm="Service Nominal"'}
	)