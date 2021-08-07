"""
命令模式
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Comand(ABC):
    @abstractmethod
    def execute(self) -> None:
        pass


class SimpleCommand(Comand):
    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCommand(Comand):
    def __init__(self, receiver: Receiver, a: str, b: str) -> None:
        self._receiver = receiver
        self._a = a
        self._b = b

    def execute(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._receiver.do_something(self._a)
        self._receiver.do_something_else(self._b)


class Receiver:
    def do_something(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def do_something_else(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class Invoker:
    def set_on_startr(self, command: Comand):
        self._on_start = command

    def set_on_finish(self, command: Comand):
        self._on_finish = command

    def to_something_important(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, Comand):
            self._on_start.execute()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, Comand):
            self._on_finish.execute()

if __name__=='__main__':
    invoker=Invoker()
    invoker.set_on_startr((SimpleCommand('Sya hi')))
    receiver=Receiver()
    invoker.set_on_finish(ComplexCommand(receiver,'send email','save report'))
    invoker.to_something_important()