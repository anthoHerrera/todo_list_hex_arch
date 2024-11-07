from typing import List
from domain.models import Todo
from domain.repository import TodoRepository

class TodoService:
    def __init__(self, repository: TodoRepository) -> None:
        self.repository = repository
        
    def create_todo(self, title: str, description: str) -> Todo:
        todo = Todo(id=None, title=title, description=description)
        self.repository.add(todo)
        return todo
    
    def get_all_todos(self) -> List[Todo]:
        return self.repository.get_all()
    
    def get_todo_by_id(self, todo_id: int) -> Todo:
        return self.repository.get_by_id(todo_id)
    
    def update_todo(self, todo_id: int, title: str, description: str, completed: bool) -> None:
        todo = self.repository.get_by_id(todo_id)
        if todo:
            todo.title = title
            todo.description = description
            todo.completed = completed
            self.repository.update(todo)
            
    def delete_todo_by_id(self, todo_id: int) -> None:
        self.repository.delete(todo_id)
        