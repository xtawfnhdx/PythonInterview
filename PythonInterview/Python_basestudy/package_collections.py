import collections


def test01():
    c1 = collections.Counter()
    c2 = collections.Counter('hello world')
    c3 = collections.Counter(e=4, b=6)
    print('c2结果:', c2)
    print('c3结果:', c3)
    print('c3 的C的结果：', c3['c'])
    c3.update('hello')
    print('c3增加后的结果：', c3)
    c3.subtract('hell')
    print('c3减少后的结果：', c3)
    del c3['h']
    print('c3删除h后的结果：', c3)
    print('转换成list:', list(c3))
    print('elements获取到的是迭代器：', c3.elements())
    print('list(elements)获取到的是详细数据：', list(c3.elements()))
    print('获取C3的前2项：', c3.most_common(2))


def test02():
    print('==============test02=====================')
    d1 = collections.Counter(a=3, b=2)
    d2 = collections.Counter(a=2, b=5, c=1)
    print('d1 + d2:', d1 + d2)
    print('d1 - d2:', d1 - d2)
    print('d1 & d2:', d1 & d2)
    print('d1 | d2:', d1 | d2)


def test03():
    dic1 = {'python': 100}
    dic2 = {'c++': 99}
    dict3 = collections.ChainMap(dic1, dic2)
    for k, v in dict3.items():
        print(k, v)


def test04():
    '''
    创建有属性名字的元组 操作  namedtuple
    :return:
    '''
    Point = collections.namedtuple('points', ['x', 'y'])
    print(issubclass(Point, tuple))
    print(type(tuple))
    point = Point(5, 6)
    print(point.x, point.y)


if __name__ == '__main__':
    test01()
    test02()
    test03()
    test04()