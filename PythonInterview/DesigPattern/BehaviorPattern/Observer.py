"""
观察者模式
"""
from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass


class ConcreteSubject(Subject):
    _state: int = None
    _observer: List[Observer] = []

    def attach(self, observer: Observer) -> None:
        self._observer.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observer.remove(observer)

    def notify(self) -> None:
        for ob in self._observer:
            ob.update(self)

    def some_business_logic(self) -> None:
        self._state = randrange(0, 10)
        self.notify()


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print('A 小于3')


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state > 4:
            print('B 等于0或者大于4')


if __name__ == '__main__':
    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()
