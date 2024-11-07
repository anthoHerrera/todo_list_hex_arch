from typing import Optional, List
from infrastructure.database import db
from domain.models import Todo
from domain.repository import TodoRepository

class TodoRepositoryImpl(TodoRepository):
    def add(self, item: Todo) -> None:
        db.session.add(item)
        db.session.commit()
    
    def get_all(self) -> List[Todo]:
        return Todo.query.all()
    
    def get_by_id(self, todo_id: int) -> Optional[Todo]:
        return Todo.query.get(todo_id)
    
    def update(self, item: Todo) -> None:
        db.session.merge(item)
        db.session.commit()

    def delete(self, item_id: int) -> None:
        todo = self.get_by_id(item_id)
        if todo:
            db.session.delete(todo)
            db.session.commit()
            