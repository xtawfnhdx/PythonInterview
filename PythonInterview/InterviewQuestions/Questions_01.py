"""
110道Python面试题
URl:
"""
# 01 一行代码实现1-100之和
# range的第二个参数，是开区间，也就是不包括第二个参数
print('第一题：', sum(range(1, 101)))

# 02 如何在一个函数内部修改全局变量
test02 = 10


def funtest02():
    global test02
    test02 = 5
    print(test02)


print('第二题：', test02)

# 03 列出5个Python 标准库
print('第三题:', 'typing', 'datetime', 'time', 'range', 'abc', 're', )

# 04 字典如何删除键和合并两个字典
test04_1 = {'a': 1, 'b': 2}
print('第四题：', test04_1)
del test04_1['a']
test04_1['c'] = 5
print(test04_1)
test04_2 = {'aa': 2, 'bb': 2}
test04_2.update(test04_1)
print(test04_2)

print('拓展，关于列表操作 list')
test04_list1 = [1, 2, 3]
test04_list2 = [4, 5, 3]
test04_list1.remove(2)
test04_list2.extend(test04_list1)
print(test04_list2)

print('拓展，关于元组 tuple')
test04_tuple = (1, 2, 3)
print(test04_tuple[1])

print('拓展，关于集合 set')
test04_set01 = {1, 2, 3}
test04_set01.remove(2)
print(test04_set01)
test04_set02 = {3, 4, 5}
test04_set02.update(test04_set01)
print(test04_set02)

# 05 谈下python的GIL
print('全局解释器锁')

# 06 python实现列表去重的方法
# 直接将列表转换为集合，集合是没有重复项的数据类型
test06_list1 = [1, 2, 3, 4, 4, 3, 7, 5, 6, 7, 3]
test06_set1 = set(test06_list1)
print('第6题的集合', test06_set1)
test06_list2 = [x for x in test06_set1]
print(test06_list2)

# 07 fun(*args,**kwargs)中的*args，**kwargs是什么意思
print('第07题：fun(*args,**kwargs)中的*args，**kwargs是什么意思')
print('*args 表示"非键值"对的可变数量的参数列表')
print('**kwargs 表示"键值对"的可变数量的参数列表')


def deftest07(*args, **kwargs):
    print('输出"非键值对"的可变数量参数列表')
    for x in args:
        print(x)
    print('输出"键值对"的可变数量参数列表')
    for k, v in kwargs.items():
        print(f'key:{k},value:{v}')


deftest07(1, 2, 4, 'aa', 'sbs', name='t2', sex='women')

# 08 python2和python3的range(100）的区别
print('第08题：python2和python3的range(100）的区别')
print('python2返回列表  python3返回迭代器 节约内存')

# 09 一句话解释什么样的语言能够用装饰器
print('09 一句话解释什么样的语言能够用装饰器')
print('函数可以作为参数传递的语言，可以使用装饰器')

# 10 Python 内建数据有哪些
print('10 Python 内建数据有哪些')
print(type(int(10)))
print(type(float(10)))
print(type(bool(0)))
print(type(str('a')))
print(type(list([1, 2])))
print(type(tuple((1, 2))))
print(type(dict({'a': 1})))
print(type(set({'a'})))
print(type(bytes()))

# 11 简述面向对象中 __new__ 和 __init__ 的区别
print('11 简述面向对象中 __new__ 和 __init__ 的区别')
print('__new__ 含义为创建一个对象的实例，为第一步操作，new方法必须有一个返回值，包含一个cls参数')
print('__init__ 含义为为对象的实例初始化一部分操作，为第二部操作，前提是已经创建了一个对象的实例')

# 12 简述with方法打开处理文件帮我们做了什么
print('12 简述with方法打开处理文件帮我们做了什么')
print('调用结束或者异常时，自动释放资源，也就是f.close方法')

# 13 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
print('13 列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]')
test13_01list = [1, 2, 3, 4, 5]


def deftest13(x):
    return x * x


test13_02list = list(map(deftest13, test13_01list))
print(test13_02list)
print('列表推导式结果：', [x for x in test13_02list if x > 10])
print('lambda表达式结果：', list(filter(lambda x: x > 10, test13_02list)))

# 14 python中生成随机整数、随机小数、0--1之间小数的方法
import random

print('生成随机整数，需要传入区间：', random.randint(1, 100))
print('生成随机小数：', random.random())
print('生成0--1之间的小数', random.random())

# 15 避免转义给字符串加哪个字母表示原始字符串？
print('15 避免转义给字符串加哪个字母表示原始字符串？')
print('输出转义字符：', '\r\n')
print('输出非转义字符(加斜杠)：', '\\r\\n')
print('输出非转义字符(加"r"字符前缀)：', r'\r\n')

# 16 正则表达式使用

# 17 python中使用断言
print('17 python中使用断言')


def deftest17(counts):
    # 断言成功，则继续执行，断言失败，则程序报错
    assert 0 < counts < 10, '这里是断言错误抛出的异常字符串'
    return counts


try:
    print('正常执行')
    deftest17(6)
    print('命中断言')
    deftest17(12)
except AssertionError as e:
    print(e)

# 18 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句
print('18 数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句')

# 19
# 20
# 21 列出python中可变数据类型和不可变数据类型，并简述原理
print('21 列出python中可变数据类型和不可变数据类型，并简述原理')
print('不可变数据类型：int,str,tuple')
print('可变数据类型：set,list,dict')
print('值修改，内存地址发生变化的，即为不可变数据类型，反之亦然')

# 22 s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
print('22 s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"')
test22_str1 = "ajldjlajfdljfddd"
test22_list1 = list(set(test22_str1))
test22_list1.sort()
print("".join(test22_list1))

# 23 用lambda函数实现两个数相乘
print('23 用lambda函数实现两个数相乘')
s = lambda x, y: x * y
print(s(2, 3))

# 24 字典根据键从小到大排序
print('24 字典根据键从小到大排序')
test24_dict1 = {'a': 1, 'c': 3, 'g': 4, 'b': 6}
test24_list1 = sorted(test24_dict1.items(), key=lambda x: x[0], reverse=False)
print(test24_list1, type(test24_list1))
test24_dict2 = dict(test24_list1)
print(test24_dict2, type(test24_dict2))

# 25 利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"
print('25 题。。。。')
import collections

test25_str1 = 'kjalfj;ldsjafl;hdsllfdhg;ldsjafl;gehr;lahfbl;ldsjafl;hl;ahlf;h'
test25_counter = collections.Counter(test25_str1.split(';'))
print(test25_counter, type(test25_counter))
print(dict(test25_counter))

# 26 正则
# 27 filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
filter函数用于过滤序列，过滤掉不符合条件的元素，返回有符合元素组成的新列表(迭代器)
filter(function,iterable)
"""
print('27题。。。。')
test27_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test27_iterable = filter(lambda x: x % 2 == 1, test27_list1)
print(list(test27_iterable))

# 28 列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('28 列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]')
test28_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test28_list2 = [x for x in test28_list1 if x % 2 == 1]
print(test28_list2)

# 29 正则re.complie作用
print('29 正则re.complie作用')
print('re.complie 是将正则表达式编译成一个对象，加快速度，并重复使用')
import re

test29_recompile = re.compile(r'^(\d{3})-(\d{3,8})$')
test29_a = test29_recompile.match('010-123456').groups()
test29_b = test29_recompile.match('202-458483').groups()
print(test29_a, test29_b)

# 30 a=（1，）b=(1)，c=("1") 分别是什么类型的数据？
print('30 a=（1，）b=(1)，c=("1") 分别是什么类型的数据？')
print('a=（1,)的类型是元组，', type((1,)))
print('b=(1)的类型是数字', type((1)))
print('c=("1")的类型是字符串', type(('1')))

# 31 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
"""
extend yu append 都可以在列表后面增加元素
extend:参数为可迭代对象，是将迭代对象的每一项挨个增加到原有列表队尾
append:参数为object，是将obj直接当做一个项增加到到列表队尾
"""
print('31 两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]')
test31_list1 = [1, 5, 7, 9]
test31_list2 = [2, 2, 6, 8]
test31_list1.extend(test31_list2)
test31_list1.sort()
print(test31_list1)
test31_list1.append(test31_list2)
print(test31_list1)
