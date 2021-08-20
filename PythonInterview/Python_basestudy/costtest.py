"""
装饰器使用
"""
import time
import functools
import decorator


def cost(func):
    @functools.wraps(func)
    def wapper(*args):
        t1 = time.time()
        res = func(*args)
        t2 = time.time()
        print(f'运行时间为:{str(t2 - t1)}')
        return res

    # return wapper()返回的是执行结果了，所以不能加括号
    return wapper


@cost
def excuteBll(a: int, b: int) -> int:
    '''
    返回两个数据的和
    :param a:第一个参数
    :param b: 第二个参数
    :return:
    '''
    time.sleep(1)
    print(a + b)


def retry(retry_count=3, sleep_time=1):
    '''
    重试装饰器
    :param retry_count:重试次数，默认3
    :param sleep_time: 等待时间，默认1
    :return:
    '''

    def inner(func):
        print('第1步')

        @functools.wraps(func)
        def wapper(*args, **kwargs):
            print('第2步')
            for i in range(retry_count):
                print('第3步')
                try:
                    print('第6步')
                    res = func(*args, **kwargs)
                    print('最后一步')
                    return res
                except:
                    print('第7步')
                    time.sleep(sleep_time)
                    continue

            return None

        return wapper

    return inner


@cost
@retry(retry_count=2, sleep_time=3)
def requestNameHttp(ip, address):
    print('第4步')
    print('请求操作中')
    time.sleep(1)
    print('请求成功')
    return


class Cust(object):
    '''
    类装饰器 核心点是__call__函数
    '''

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('装饰器装饰')
        f = self.func(*args, **kwargs)
        print('装饰完成了')
        return f


@Cust
def test02(a: int, b: int) -> int:
    '''
    返回两个数相加结果
    :param a:
    :param b:
    :return:
    '''
    print('函数内部')
    print(f'a+b={a + b}')


@decorator.decorator
def costss(func, time_sleep=3, *args, **kw):
    print('开始了')
    f = func(*args, **kw)
    print('结束了')
    return f


@costss
def costssTest(a, b):
    print(f'a+b={a + b}')


if __name__ == '__main__':
    # excuteBll(3, 4)
    # print(excuteBll.__name__)
    # print(excuteBll.__doc__)
    print('=====================')
    requestNameHttp('', '')
    print('=====================')
    test02(3, 4)
    # print(test02.__name__)
    # print(test02.__doc__)
    print('=====================')
    costssTest(3, 4)
