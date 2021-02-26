from flask import make_response
from app import app

# Status Check Route
@app.route('/status', methods=['GET'])
def statusCheck():
	return make_response(
		'Site is Active',
		200,
		{'WWW-Authenticate': 'Basic Realm="Service Nominal"'}
	)

# Bad Request
@app.errorhandler(400)
def page_not_found(e):
	return make_response(
		'Bad Request',
		400,
		{'WWW-Authenticate': 'Basic Realm="HTTP Request Issue"'}
	)

# Unauthorized
@app.errorhandler(401)
def unauthorized_request(e):
	return make_response(
		'Unauthorized',
		401,
		{'WWW-Authenticate': 'Basic Realm="Action/Request Unauthorized"'}
	)

# Forbidden
@app.errorhandler(403)
def forbidden_action(e):
	return make_response(
		'Forbidden',
		403,
		{'WWW-Authenticate': 'Basic Realm="Action/Request Forbidden"'}
	)

# Page Not Found
@app.errorhandler(404)
def page_not_found(e):
	return make_response(
		'Page/Resource Not Found',
		404,
		{'WWW-Authenticate': 'Basic Realm="Page/Resource Not Found"'}
	)

# Bad Request
@app.errorhandler(405)
def wrong_http_method(e):
	return make_response(
		'Method Not Allowed',
		405,
		{'WWW-Authenticate': 'Basic Realm="Unsupported HTTP Method"'}
	)

# Internal Server Error
@app.errorhandler(500)
def internal_server_error(e):
	return make_response(
		'Internal Server Error',
		500,
		{'WWW-Authenticate': 'Basic Realm="Internal Server Error"'}
	)

# Not Implemented
@app.errorhandler(501)
def not_implemented(e):
	return make_response(
		'Feature/Method Not Implemented',
		500,
		{'WWW-Authenticate': 'Basic Realm="Not Implemented"'}
	)