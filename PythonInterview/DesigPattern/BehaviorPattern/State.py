"""
状态模式
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    # 状态(状态模式的判断)
    _state: State = None

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State) -> None:
        # 根据不同状态，切换上下文
        self._state = state
        self._state.context = self

    # 最终执行器的操作
    def request1(self):
        self._state.handle1()

    def request2(self):
        self._state.handle2()


class State(ABC):
    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class ConcreteStateA(State):
    def handle1(self) -> None:
        print('执行了A—1')
        self.context.transition_to(ConcreteStateB())

    def handle2(self) -> None:
        print('执行了A-2')


class ConcreteStateB(State):
    def handle1(self) -> None:
        print('执行了B—1')

    def handle2(self) -> None:
        print('执行了B—2')
        self.context.transition_to(ConcreteStateA())


if __name__ == '__main__':
    context = Context(ConcreteStateA())
    context.request1()
    context.request2()
    context.request2()
