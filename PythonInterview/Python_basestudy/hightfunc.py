"""
高阶函数学习
"""


def test01():
    exp_01 = '3+7*2'
    c = compile(exp_01, '', 'eval')
    res = eval(c)
    print(f'3+7*2={res}')

    exp_02 = 'print("hello world")'
    t2 = compile(exp_02, '', 'single')
    exec(t2)

    exp_03 = 'for i in range(3):print(i)'
    t3 = compile(exp_03, '', 'exec')
    exec(t3)

    exp_04 = '''def max(a, b):
        max_value = b
        if a > b:
            max_value = a
        print('max value is {value}'.format(value=max_value))
    '''
    t4 = compile(exp_04, '', 'exec')
    exec(t4)
    # print(globals())
    print(locals())
    t4_func = locals()['max']
    print(t4_func.__name__)
    t4_func(3, 4)


def test02():
    def test_01(name, id):
        prstr = 'this name is {name},id is {id}'.format(name=name, id=id)
        print(prstr)

    def test_02(name, id):
        prstr = 'this name is {name},id is {id}'.format(**locals())
        print(prstr)

    test_01('zhangsan', '123')
    test_01('lisi', '45')


def test03():
    pass


def test04():
    pass


def test05():
    pass


def test06():
    pass


def test07():
    pass


def test08():
    pass


if __name__ == '__main__':
    test01()
    test02()
    test03()
    test04()
    test05()
    test06()
    test07()
    test08()
