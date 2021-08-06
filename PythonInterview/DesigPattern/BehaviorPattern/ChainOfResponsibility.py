"""
责任链模式
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    @abstractmethod
    def setNext(self, h: Handler) -> Handler:
        pass

    @abstractmethod
    def handler(self,request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    _next: Handler = None

    def setNext(self, h: Handler) -> Handler:
        self._next = h
        return h

    @abstractmethod
    def handler(self, request: Any) -> Optional[str]:
        if self._next:
            return self._next.handler(request)
        return None


class MonkeyHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey:I'll eat the {request}"
        else:
            return super().handler(request)


class SquirrelHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handler(request)


class DogHandler(AbstractHandler):
    def handler(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handler(request)


def client_code(h: Handler) -> None:
    for food in ["Nut", "Banana", "Cup of coffee"]:
        print(f"\nClient: Who wants a {food}?")
        result = h.handler(food)
        if result:
            print(f"  {result}", end="")
        else:
            print(f"  {food} was left untouched.", end="")


if __name__ == '__main__':
    m = MonkeyHandler()
    s = SquirrelHandler()
    d = DogHandler()
    m.setNext(s).setNext(d)
    print("Chain: Monkey > Squirrel > Dog")
    client_code(m)
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(s)
