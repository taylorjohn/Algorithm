# Implement Stack

from typing import Any


class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def push(self, value: Any) -> None:
        self.data.append(value)

    def pop(self) -> Any:
        return self.data.pop()
