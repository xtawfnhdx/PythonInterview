"""
类的初始化各个函数调用方式
"""


class A:
    def __init__(self):
        print('__init__')
        print(self)
        self.a = 10
        self.b = 20

    def __new__(cls, *args, **kwargs):
        print('__new__')
        new = super().__new__(cls, *args, **kwargs)
        print(new)
        return new

    def __call__(self, *args, **kwargs):
        print('__call__')
        print(self)

    def show(self):
        print(f'msg {self.a}')


a = A()
print(callable(a))
a.show()
# a为可调用对象，直接对对象执行（），即可调用call函数
a()


class Count:
    def __init__(self, func):
        self.func = func
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1
        return self.func(*args, **kwargs)


@Count
def foo():
    pass


for i in range(10):
    foo()

print(foo.count)
