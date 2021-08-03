"""
组合模式
"""

from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def excute(self):
        pass


class P1(Person):
    def __init__(self, name, job):
        self.name = name
        self.job = job
        self.child = []

    def add(self, p: Person):
        self.child.append(p)

    def remove(self, p: Person):
        self.child.remove(p)

    def excute(self):
        print(f"{self.name} 的工作是 {self.job}")
        for x in self.child:
            print(f"{self.name} 的员工是 {x.name}")


if __name__ == '__main__':
    p1 = P1('张三', '经理')
    p2 = P1('李四', '副经理')
    p1.add(p2)
    p1.excute()
    p1.remove(p2)
    p1.excute()
