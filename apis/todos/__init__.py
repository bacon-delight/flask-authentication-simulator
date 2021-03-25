from flask import Blueprint, request, make_response, jsonify
import requests

# Decorators
from decorators.validateToken import validateToken

# Blueprint Prefix
todos = Blueprint('todos', __name__)



# ------------------------ Routes ------------------------
@todos.route('/', methods=['GET'])
@validateToken
def getAllTodos():
	response = requests.get("https://jsonplaceholder.typicode.com/todos")
	return make_response(jsonify(response.json()))

@todos.route('/<todo_id>', methods=['GET'])
@validateToken
def getTodoDetails(todo_id):
	response = requests.get("https://jsonplaceholder.typicode.com/todos/" + todo_id)
	return make_response(jsonify(response.json()))

@todos.route('/', methods=['POST'])
@validateToken
def addTodo():
	response = requests.post("https://jsonplaceholder.typicode.com/todos", data = request.get_json())
	return make_response(jsonify(response.json()))

@todos.route('/<todo_id>', methods=['PUT'])
@validateToken
def updateTodo(todo_id):
	response = requests.put("https://jsonplaceholder.typicode.com/todos/" + todo_id, data = request.get_json())
	return make_response(jsonify(response.json()))

@todos.route('/<todo_id>', methods=['DELETE'])
@validateToken
def deleteTodo(todo_id):
	response = requests.delete("https://jsonplaceholder.typicode.com/todos/" + todo_id)
	return make_response(jsonify(response.json()))