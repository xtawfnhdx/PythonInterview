"""
模板方法模式
"""
from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def temp_method(self) -> None:
        """
        模板流程
        :return:
        """
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()
        self.required_operations2()
        self.base_operation3()
        self.hook2()

    # 模板具体的步骤
    def base_operation1(self) -> None:
        print('baseoperation1 执行')

    def base_operation2(self) -> None:
        print('baseoperation2 执行')

    def base_operation3(self) -> None:
        print('baseoperation3 执行')

    def required_operations1(self) -> None:
        pass

    def required_operations2(self) -> None:
        pass

    def hook1(self) -> None:
        pass

    def hook2(self) -> None:
        pass


# 针对模板的具体实现
class ConcreteClass1(AbstractClass):
    def required_operations1(self) -> None:
        print('class1执行required1')

    def required_operations2(self) -> None:
        print('class1执行required2')


# 针对模板的具体实现
class ConcreteClass2(AbstractClass):
    def required_operations1(self) -> None:
        print('class2执行required1')

    def required_operations2(self) -> None:
        print('class2执行required2')

    def hook2(self) -> None:
        print('class2执行hook2')


def client_code(abstract_clas: AbstractClass) -> None:
    abstract_clas.temp_method()


if __name__ == '__main__':
    print('-----------------------')
    client_code(ConcreteClass1())
    print('-----------------------')
    client_code(ConcreteClass2())
