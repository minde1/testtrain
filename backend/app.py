from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user data storage (sample database)
users_db = {
    1: {"name": "Alice", "email": "alice@example.com", "age": 30, "married": True},
    2: {"name": "Bob", "email": "bob@example.com", "age": 25, "married": False},
    3: {"name": "Osama", "email": "osama@example.com", "age": 15, "married": False},
    4: {"name": "Shakir", "email": "shakir@example.com", "age": 41, "married": True}

}

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    print("asdfsadf")
    return jsonify(users_db)

# GET a specific user by email
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users_db.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# CREATE a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_id = max(users_db.keys(), default=0) + 1
    users_db[new_id] = {
        "name": data.get("name"),
        "email": data.get("email"),
        "age": data.get("age"),
        "married": data.get("married")
    }
    return jsonify({"id": new_id, "message": "User created successfully","users":users_db}), 201

# UPDATE an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id not in users_db:
        return jsonify({"error": "User not found"}), 404
    data = request.json
    users_db[user_id].update({
        "name": data.get("name"),
        "email": data.get("email"),
        "age": data.get("age"),
        "married": data.get("married")
    })
    return jsonify({"message": "User updated successfully","users":jsonify(users_db)})

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users_db:
        del users_db[user_id]
        return jsonify({"message": "User deleted successfully"})
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    # Specify the port number (e.g., 5001) and optionally the host
    app.run(host='0.0.0.0', port=5001, debug=True)