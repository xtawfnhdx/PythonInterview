import functools
import os


def test01():
    dest_join = functools.partial(os.path.join, '.\dest')
    os.rmdir(dest_join('dir1'))
    os.rmdir(dest_join('dir2'))

    os.mkdir(dest_join('dir1'))
    os.mkdir(dest_join('dir2'))

    def test(x: int, y: int) -> int:
        return x + y

    add_fun = functools.partial(test, 5)
    print(add_fun(5))
    print(add_fun(2))


def test02():
    """
    singledispatch 将函数注册成泛型，并针对不同的类型执行操作
    :return:
    """

    class Man(object):
        def haha(self):
            print('一个男人')

    class Monkey(object):
        def haha(self):
            print('一只猴子')

    @functools.singledispatch
    def showMsg(obj):
        print('什么也不是')

    @showMsg.register(Man)
    def manhaha(obj):
        obj.haha()

    @showMsg.register(Monkey)
    def monkeyhaha(obj):
        obj.haha()

    man = Man()
    monkey = Monkey()
    print('===========================')
    showMsg(man)
    showMsg(monkey)


def test03():
    list1 = [2, 3, 4, 5, 5, 65, 6, 7]
    res = functools.reduce(lambda x, y: x * y, list1)


def test04():
    def cost(func):
        # functools.wraps保留装饰器装饰以后丢失的信息,如名字，使用文档等
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            pass

        return wrapper

    @cost
    def test(sleep_time):
        """
        测试装饰器
        :param sleep_time:休眠时间
        :return: 空
        """
        pass

    print(test.__name__)
    print(test.__doc__)


if __name__ == '__main__':
    test01()
    test02()
    test03()
    test04()
