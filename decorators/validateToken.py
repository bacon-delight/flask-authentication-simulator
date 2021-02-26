from flask import request, abort
from functools import wraps
from app import app
from jwt import decode


def validateToken(function):

	@wraps(function)

	def wrapper(*args, **kwargs):

		# Get token from header
		try:
			token = request.headers.get('Authorization').split(" ")[1]
		except:
			return abort(401)

		# Attempt to Decode Token
		try:
			decode(token, app.config['SECRET_KEY'], algorithms="HS256")
		except:
			return abort(401)

		return function(*args, **kwargs)

	return wrapper