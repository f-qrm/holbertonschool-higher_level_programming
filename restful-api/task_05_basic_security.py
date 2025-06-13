#!/usr/bin/python3
"""
Flask API implementing HTTP Basic Authentication and JWT-based authentication.

This module provides a Flask web API with the following features:
- HTTP Basic Authentication using username and password.
- JWT (JSON Web Token) authentication for protected endpoints.
- Role-based access control (e.g., admin-only endpoints).
- Custom error handlers for JWT errors (invalid token, expired token, etc.).

Attributes:
    app (Flask): The Flask application instance.
    jwt (JWTManager): Manages JWT creation and validation.
    auth (HTTPBasicAuth): Handles HTTP Basic Auth.
    users (dict): In-memory storage of user data (username, hashed password,
    role).
"""
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask import Flask
from flask import jsonify
from flask import request
from flask_jwt_extended import JWTManager
from flask_jwt_extended import create_access_token
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity


app = Flask(__name__)
jwt = JWTManager(app)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'Key_2532'
users = {
    "user1": {"username": "user1", "password":
              generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password":
               generate_password_hash("password"), "role": "admin"}
}


@auth.verify_password
def verify_password(username, password):
    """
    Verify the username and password for HTTP Basic Auth.

    Args:
        username (str): The username provided by the client.
        password (str): The password provided by the client.

    Returns:
        bool: True if authentication succeeds, False otherwise.
    """
    if username in users:
        hashed_password = users[username]["password"]
        if check_password_hash(hashed_password, password):
            return users[username]
    return None


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """
    HTTP Basic Auth protected endpoint.

    Returns:
        Response: JSON message indicating access is granted.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login_jwt():
    """
    Login endpoint to generate a JWT token.

    Expects:
        JSON payload with "username" and "password".

    Returns:
        Response: JSON containing the access token if credentials are valid,
                  or error message with status 401 otherwise.
    """
    username = request.json.get("username")
    password = request.json.get("password")
    if username not in users or not (
        check_password_hash(users.get(username)['password'], password)
    ):
        return jsonify({"error": "Invalid username or password"}), 401
    access_token = create_access_token(identity={
        "username": username,
        "role": users[username]["role"]
        })
    return jsonify(access_token=access_token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    JWT-protected endpoint.

    Returns:
        Response: JSON message indicating JWT access is granted.
    """
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    """
    JWT-protected admin-only endpoint.

    Returns:
        Response: JSON success message if user is admin,
                  or error message with status 403 otherwise.
    """
    verif = get_jwt_identity()
    if verif['role'] != 'admin':
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid JWT token.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON error response with status 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid JWT token.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON error response with status 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired JWT token.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON error response with status 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked JWT token.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON error response with status 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle case where a fresh JWT token is required.

    Args:
        err (str): Error message.

    Returns:
        Response: JSON error response with status 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
