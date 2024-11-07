from abc import ABC, abstractmethod
from typing import Optional, List

class TodoRepository(ABC):
    @abstractmethod
    def add(self, item: 'Todo') -> None:
        pass

    @abstractmethod
    def get_all(self) -> List['Todo']:
        pass

    @abstractmethod
    def get_by_id(self, todo_id: int) -> Optional['Todo']:
        pass

    @abstractmethod
    def update(self, item: 'Todo') -> None:
        pass

    @abstractmethod
    def delete(self, item_id: int) -> None:
        pass
    