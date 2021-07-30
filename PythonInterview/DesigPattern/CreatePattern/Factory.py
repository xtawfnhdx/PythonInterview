from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def create_table(self) -> AttributeMsg:
        pass

    @abstractmethod
    def create_chair(self) -> AttributeMsg:
        pass


class AttributeMsg(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getAttribute(self) -> str:
        return f"name:{self.name},price:{self.price}"


class Factory1(Factory):
    def create_table(self):
        return Table1("f1_tab", 111)

    def create_chair(self):
        return Chair1("f1_cha", 222)


class Factory2(Factory):
    def create_table(self):
        return Table2("f2_tab", 333)

    def create_chair(self):
        return Chair2("f2_cha", 444)


class Table1(AttributeMsg):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Table2(AttributeMsg):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Chair1(AttributeMsg):
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Chair2(AttributeMsg):
    def __init__(self, name, price):
        self.name = name
        self.price = price


def create_furniture(fa: Factory):
    chair = fa.create_chair()
    print(chair.getAttribute())

    tab = fa.create_table()
    print(tab.getAttribute())


if __name__ == "__main__":
    create_furniture(Factory1())
    create_furniture(Factory2())
