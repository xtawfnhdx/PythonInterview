"""
生成器模式
生产不同配置的汽车
1：普通汽车
2：普通汽车+定制颜色+定制轮胎
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class BuilderCar(ABC):
    @abstractmethod
    def setcolor(self) -> None:
        pass

    @abstractmethod
    def settyre(self) -> None:
        pass


class BuilderFactoryA(BuilderCar):
    """
    具体生成器1：支持构建颜色，轮胎
    """

    def __init__(self):
        self._car = Car()

    def setcolor(self, color) -> None:
        self._car.color = color

    def settyre(self, tyre) -> None:
        self._car.tyre = tyre

    def getCarMsg(self) -> str:
        return f"car msg :color:{self._car.color},tyre:{self._car.tyre}"


class BuilderFactoryB(BuilderCar):
    """
    具体生成器1：支持构建颜色，不支持自定义轮胎
    """

    def __init__(self):
        self._car = Car()

    def setcolor(self, color) -> None:
        self._car.color = color

    def settyre(self) -> None:
        pass

    def getCarMsg(self) -> str:
        return f"car msg :color:{self._car.color},tyre:{self._car.tyre}"


class Car():
    def __init__(self):
        self._color = "write"
        self._tyre = "min"

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def tyre(self):
        return self._tyre

    @tyre.setter
    def tyre(self, tyre):
        self._tyre = tyre


class Directry:
    """
    主管，负责管理生产什么车型
    """

    def createRedCar(self) -> str:
        car = BuilderFactoryB()
        car.setcolor("red")
        return car.getCarMsg()

    def createDefault(self) -> str:
        car = BuilderFactoryB()
        return car.getCarMsg()

    def createBlueMax(self) -> str:
        car = BuilderFactoryA()
        car.setcolor("blue")
        car.settyre("max")
        return car.getCarMsg()


if __name__ == "__main__":
    dic = Directry()
    print(dic.createDefault())
    print(dic.createRedCar())
    print(dic.createBlueMax())

# from __future__ import annotations
# from abc import ABC, abstractmethod
# from typing import Any
#
#
# class Builder(ABC):
#     """
#     生成器(虚拟类)
#     """
#     @property
#     @abstractmethod
#     def product(self) -> None:
#         pass
#
#     @abstractmethod
#     def product_par_a(self) -> None:
#         pass
#
#     @abstractmethod
#     def product_par_b(self) -> None:
#         pass
#
#     @abstractmethod
#     def product_par_c(self) -> None:
#         pass
#
#
# class ConcreteBuilder(Builder):
#     """
#     具体生成器
#     """
#     def __init__(self) -> None:
#         self.reset()
#
#     def reset(self) -> None:
#         self._product = Product1()
#
#     @property
#     def product(self) -> Product1:
#         product = self._product
#         self.reset()
#         return product
#
#     def product_par_a(self) -> None:
#         self._product.add('PartA1')
#
#     def product_par_b(self) -> None:
#         self._product.add('PartB1')
#
#     def product_par_c(self) -> None:
#         self._product.add('PartC1')
#
#
# class Product1():
#     def __init__(self) -> None:
#         self.parts = []
#
#     def add(self, part: Any) -> None:
#         self.parts.append(part)
#
#     def list_parts(self) -> None:
#         print(f"Product parts:{','.join(self.parts)}", end="")
#
#
# class Director:
#     """
#     主管（主管使用生成器）
#     """
#     def __init__(self) -> None:
#         self._builder = None
#
#     @property
#     def builder(self) -> Builder:
#         return self._builder
#
#     @builder.setter
#     def builder(self, builder: Builder) -> None:
#         self._builder = builder
#
#     def build_minman_viable_product(self) -> None:
#         self._builder.product_par_a()
#
#     def build_maxman_viable_product(self) -> None:
#         self._builder.product_par_a()
#         self._builder.product_par_b()
#         self._builder.product_par_c()
#
#
# if __name__ == "__main__":
#     """
#     客户端
#     """
#     dir=Director()
#     con=ConcreteBuilder()
#     dir.builder=con
#     dir.build_minman_viable_product()
#     con.product.list_parts()
#
#
