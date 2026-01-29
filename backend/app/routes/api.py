from flask import Blueprint, jsonify, request
from ..controllers.user_controller import UserController
from ..models.user import User

api_bp = Blueprint("api", __name__)

@api_bp.route("/users", methods=["GET"])
def get_users():
    users = UserController.get_users()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

@api_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = UserController.get_user(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "name": user.name, "email": user.email})

@api_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    user = User(id=data.get("id"), name=data.get("name"), email=data.get("email"))
    result = UserController.create_user(user)
    return jsonify({"id": result.id, "name": result.name, "email": result.email}), 201 