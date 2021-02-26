from jwt import encode
from datetime import datetime, timedelta
from app import app


def generateToken(minutes):

	# Encode Token
	return encode({
			'iss': app.config['TOKEN_ISSUER'],
			'iat': datetime.utcnow(),
			'exp': datetime.utcnow() + timedelta(minutes=minutes)
		},
		app.config['SECRET_KEY'],
		algorithm=app.config['ENCRYPT_ALGORITHM']
	)