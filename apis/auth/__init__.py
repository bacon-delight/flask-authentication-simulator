from flask import Blueprint, request

# Components
from .components.processLogin import processLogin
from .components.processRefresh import processRefresh

# Decorators
from decorators.validateToken import validateToken

# Blueprint Prefix
auth = Blueprint('auth', __name__)



# ------------------------ Routes ------------------------
@auth.route('/login', methods=['GET'])
def login():
	return processLogin(auth = request.authorization)

@auth.route('/refresh', methods=['GET'])
@validateToken
def refresh():
	return processRefresh()