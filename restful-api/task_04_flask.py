#!/usr/bin/env python3
"""
Flask-based RESTful API for basic user management.

This API provides a set of HTTP endpoints for managing a collection of
users stored
in memory. It supports reading the list of users, checking API status,
retrieving
individual user data, and adding new users via POST requests.

Routes:
    - GET '/'             : Returns a welcome message.
    - GET '/data'         : Returns a list of all registered usernames in
    JSON format.
    - GET '/status'       : Returns the plain text message 'OK'.
    - GET '/users/<username>' : Returns user data if the username exists,
    or a 404 error.
    - POST '/add_user'    : Adds a new user using JSON data containing at
    least a 'username' field.

Modules:
    flask: Web framework used to create the API.

Usage:
    Run this script to start the Flask development server on port 5000.
    Example request:
        curl -X POST -H "Content-Type: application/json" \
        -d '{"username": "fjolla", "age": 25}' http://localhost:5000/add_user

Note:
    All user data is stored in a volatile in-memory dictionary (`users`), and
    will be
    lost when the server restarts.
"""
from flask import Flask
from flask import jsonify
from flask import request


app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Return a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def data():
    """Return the list of all usernames."""
    return jsonify(list(users.keys())), 200


@app.route('/status', methods=['GET'])
def stat():
    """Return the status message 'OK'."""
    return 'OK'


@app.route('/users/<username>')
def uname(username):
    """Return the user's data if found, or a 404 error."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def adduser():
    """Add a new user to the system using JSON input."""
    new_user = request.get_json()
    if "username" in new_user:
        user2 = new_user["username"]
        users[user2] = new_user
        print(user2)
        return jsonify({"message": "User added", "user": new_user}), 201
    else:
        return jsonify({"error": "Username is required"}), 400


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
