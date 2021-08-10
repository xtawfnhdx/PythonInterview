"""
策略模式
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, List


class Context():
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_something_business_logic(self) -> None:
        result = self._strategy.do_algorithm(['a', 'b', 'c', 'd', 'e', 'f'])
        print(''.join((result)))


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List) -> Any:
        pass


# 定义"A"种策略
class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List) -> Any:
        return sorted(data)


# 定义"B"种策略
class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List) -> Any:
        return reversed(sorted(data))


if __name__ == '__main__':
    context = Context(ConcreteStrategyA())
    context.do_something_business_logic()
    context.strategy = ConcreteStrategyB()
    context.do_something_business_logic()
