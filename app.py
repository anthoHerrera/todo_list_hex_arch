from time import sleep
from flask import Flask, request, jsonify
from infrastructure.database import db, init_db
from infrastructure.config import Config
from infrastructure.repositories import TodoRepositoryImpl
from application.services import TodoService

app = Flask(__name__)
app.config.from_object(Config)

sleep(3)

db.init_app(app)
init_db(app)

todo_repository = TodoRepositoryImpl()
todo_service = TodoService(todo_repository)

@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.json
    if not data.get("title") or not data.get("description"):
        return jsonify({"error": "title and description are required"}), 400
    todo = todo_service.create_todo(
        data["title"],
        data["description"]
    )
    return jsonify(todo.to_dict()), 201

@app.route("/todos", methods=["GET"])
def get_todos():
    todos = todo_service.get_all_todos()
    return jsonify([todo.to_dict() for todo in todos])

@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404
    return jsonify(todo.to_dict())

@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):
    data = request.json
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404
    
    # update fields
    todo.title = data.get("title", todo.title)
    todo.description = data.get("description", todo.description)
    todo.completed = data.get("completed", todo.completed)
    
    # save the updated Todo item
    todo_service.update_todo(
        todo.id,
        todo.title,
        todo.description,
        todo.completed
    )
    return jsonify(todo.to_dict()), 200

@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = todo_service.get_todo_by_id(todo_id)
    if not todo:
        return jsonify({"error": "todo not found"}), 404
    todo_service.delete_todo_by_id(todo_id)
    return jsonify({"message": "todo deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)