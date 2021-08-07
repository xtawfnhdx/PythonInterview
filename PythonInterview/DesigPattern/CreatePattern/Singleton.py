"""
使用元类来创建单例
"""


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances


class Singleton(metaclass=SingletonMeta):
    def some_business_logic(self):
        pass


class SingTye():
    """
    使用 new 方式来构造元类
    """
    _sing = None

    def __new__(cls, *args, **kwargs):
        if not cls._sing:
            cls._sing = super().__new__(cls, *args, **kwargs)
        return cls._sing


if __name__ == "__main__":
    # 方式1
    s1 = Singleton()
    s2 = Singleton()
    if id(s1) == id(s2):
        print("相同")
    else:
        print("不同")

    # 方式2
    b1 = SingTye()
    b2 = SingTye()
    print(b1, b2)
    if id(b1) == id(b2):
        print('相同')
    else:
        print('不同')
