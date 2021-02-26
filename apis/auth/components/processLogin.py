from flask import abort, make_response, jsonify
from app import app
from .generateToken import generateToken


def processLogin(auth):

	# Check if Credential(s) are Missing
	if not auth or not auth.username or not auth.password:
		return abort(401)

	# Validate Credentials
	if not auth.username==app.config['CREDENTIALS_USERNAME'] or not auth.password==app.config['CREDENTIALS_PASSWORD']:
		return abort(401)

	# Return Tokens
	return make_response(
		jsonify(
			{
				'access-token': generateToken(minutes=app.config['ACCESS_TOKEN_LIFETIME']),
				'refresh-token': generateToken(minutes=app.config['REFRESH_TOKEN_LIFETIME'])
			}
		)
	)