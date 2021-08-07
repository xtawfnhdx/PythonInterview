from abc import ABC, abstractmethod


class Component(ABC):
    """
    基本组件接口
    """

    @abstractmethod
    def operation(self) -> str:
        """
        定义具体操作
        :return:
        """
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "基本组件的基础实现"


class Decorator(Component):
    """
    装饰器遵循与基本组件的接口(继承)
    """
    _comment: Component = None

    def __init__(self, comment: Component):
        self._comment = comment

    @property
    def comment(self) -> Component:
        return self._comment

    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"A装饰器 {self.comment.operation()}"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"B装饰器 {self.comment.operation()}"


def client_code(comment: Component) -> None:
    print("执行结果", end="\n")
    print(comment.operation())


if __name__ == '__main__':
    simple = ConcreteComponent()
    client_code(simple)

    ca = ConcreteDecoratorA(simple)
    client_code(ca)

    cb = ConcreteDecoratorB(ca)
    client_code(cb)

# """
# 装饰模式
# """
# from __future__ import annotations
# from abc import ABC, abstractmethod
#
#
# class IHouse(ABC):
#     @abstractmethod
#     def live(self):
#         pass
#
#
# class House(IHouse):
#     def live(self):
#         print('房子基本功能-居住')
#
#
# class IMirrorHouse(IHouse):
#     @abstractmethod
#     def lookMirror(self):
#         pass
#
#
# class MirrorHouse(IMirrorHouse):
#     def __init__(self, se):
#         self = se
#
#     def lookMirror(self):
#         print('有了镜子功能')
#
#
# if __name__ == '__main__':
#     house = House()
#     house.live()
#     m = MirrorHouse(house)
#     m.live()
#     m.lookMirror()
