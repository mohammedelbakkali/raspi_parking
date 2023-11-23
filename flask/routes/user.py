# controllers/routes.py

from flask import jsonify, request
from app import app
from controllers.userController import get_all_users, add_user, update_user, delete_user, get_user_by_id

@app.route('/')
def index():
    users = get_all_users()
    return jsonify(users)

@app.route('/api/add_user', methods=['POST'])
def add_user_api():
    try:
        user_data = request.get_json()
        name = user_data['name']
        email = user_data['email']
        add_user(name, email)

        response = {'status': 'success', 'message': 'User added successfully'}
        return jsonify(response)

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return jsonify(response), 500

@app.route('/api/update_user/<int:user_id>', methods=['PUT'])
def update_user_api(user_id):
    try:
        user_data = request.get_json()
        name = user_data['name']
        email = user_data['email']
        update_user(user_id, name, email)

        response = {'status': 'success', 'message': 'User updated successfully'}
        return jsonify(response)

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return jsonify(response), 500

@app.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user_api(user_id):
    try:
        delete_user(user_id)

        response = {'status': 'success', 'message': 'User deleted successfully'}
        return jsonify(response)

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return jsonify(response), 500

@app.route('/api/get_user/<int:user_id>', methods=['GET'])
def get_user_api(user_id):
    try:
        user = get_user_by_id(user_id)

        if user:
            response = {'status': 'success', 'user': user}
        else:
            response = {'status': 'error', 'message': 'User not found'}

        return jsonify(response)

    except Exception as e:
        response = {'status': 'error', 'message': str(e)}
        return jsonify(response), 500
