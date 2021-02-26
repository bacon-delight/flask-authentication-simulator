from flask import make_response, jsonify
from app import app
from .generateToken import generateToken


def processRefresh():

	# Return Tokens
	return make_response(
		jsonify(
			{
				'access-token': generateToken(minutes=app.config['ACCESS_TOKEN_LIFETIME']),
				'refresh-token': generateToken(minutes=app.config['REFRESH_TOKEN_LIFETIME'])
			}
		)
	)