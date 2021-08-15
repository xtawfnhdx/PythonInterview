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

# 32 用python删除文件和用linux命令删除文件方法
print('32 用python删除文件和用linux命令删除文件方法')
print(f'python方法：os.remove')
print(f'linux:rm')

# 33 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
print('33 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”')
import datetime

# strftime 时分秒(H M S)都要大写
test32_str1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(test32_str1)

# 33 数据库优化查询方法

# 34 请列出你会的任意一种统计图(条形图，折线图等)绘制的开源库，第三方也行
print('34 请列出你会的任意一种统计图(条形图，折线图等)绘制的开源库，第三方也行')
print('pyecharts', 'matplotlib')

# 35 写一段自定义异常代码
print('35 写一段自定义异常代码')


def def35():
    try:
        raise IndexError('测试测试')
    except IndexError as i:
        print(i)


def35()

# 36 正则表达式匹配中，(.*)和(.*?)匹配的区别？
print('36 正则表达式匹配中，(.*)和(.*?)匹配的区别？')
print('(.*) 是贪婪匹配，尽可能多的往后面匹配')
print('(.*？) 非贪婪匹配，尽可能少的匹配')
import re

test36_str = '<a>哈哈</a><a>呵呵</a>'
test36_re1 = re.findall("<a>(.*)</a>", test36_str)
test36_re2 = re.findall("<a>(.*?)</a>", test36_str)
print(test36_re1)
print(test36_re2)

# 38 简述Django的orm
print('38 简述Django的orm')
print('后续补充')

# 39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
print('39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]')
test39_list1 = [[1, 2], [3, 4], [5, 6]]
# 使用列表推导式 for i in a
test39_list2 = [j for i in test39_list1 for j in i]
print(test39_list2)

# 40 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
print('40 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果')
test40_str1 = 'abc'
test40_str2 = 'def'
test40_list1 = ['d', 'e', 'f']
print(test40_str1.join(test40_str2))
test40_str1 = 'abc'
test40_str2 = 'def'
test40_list1 = ['d', 'e', 'f']
print(test40_str1.join(test40_list1))

# 41 举例说明异常模块中try except else finally的相关意义
print('41 举例说明异常模块中try except else finally的相关意义')

# 42 python中交换两个数值
print('42 python中交换两个数值')
test42_i1, test42_i2 = 3, 4
print(test42_i1, test42_i2)
test42_i1, test42_i2 = test42_i2, test42_i1
print(test42_i1, test42_i2)

# 43 举例说明zip（）函数用法
print('43 举例说明zip（）函数用法')
test43_list1 = [1, 2, 3, 4, 5]
test43_list2 = ['a', 'b', 'c', 'd', 'e']
test43_res1 = zip(test43_list1, test43_list2)
print(list(test43_res1))

# 44 a="张明 98分"，用re.sub，将98替换为100
print('44 a="张明 98分"，用re.sub，将98替换为100')
test44_str1 = "张明 98分"

# 45 写5条常用sql语句

# 46 a="hello"和b="你好"编码成bytes类型
print('46 a="hello"和b="你好"编码成bytes类型')
test46_str1 = "hello"
test46_str2 = "你好"
print(test46_str1.encode())
print(test46_str2.encode(encoding='utf-8'))

# 47 [1,2,3]+[4,5,6]的结果是多少？
print('47 [1,2,3]+[4,5,6]的结果是多少？')
test47_list1 = [1, 2, 3]
test47_list2 = [4, 5, 6]
# +与extend相同
print(test47_list1 + test47_list2)
test47_list1.extend(test47_list2)
print(test47_list1)

# 48 提高python运行效率的方法
print('48 提高python运行效率的方法')
print(r'使用生成器，节约内存')
print(r'循环代码优化，避免过多重复代码')
print(r'多线程，多进程，协程')
print(r'多个判断，命中率高的放到最前面')

# 49 简述mysql和redis区别
print('49 简述mysql和redis区别')
print('存储方式不一样，'
      'mysql是关系数据库，数据主要固化到磁盘中'
      'redis是以键值对存储的菲关系数据库，数据主要保存在内存中')

# 50 遇到bug如何处理

# 51 正则匹配，匹配日期2018-03-20

# 52 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
print('52 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]')
test52_list1 = [2, 3, 5, 4, 9, 6]
test52_set = set(test52_list1)
test52_list2 = list(test52_set)
print(test52_list2)

# 53 写一个单列模式
print('53 写一个单列模式')


class Cls53():
    _cls = None

    def __new__(cls, *args, **kwargs):
        if not cls._cls:
            _cls = super().__new__(cls)
        return cls._cls


test53_t1 = Cls53()
test53_t2 = Cls53()
print(id(test53_t1))
print(id(test53_t2))

# 54 保留两位小数
test54_float = 3.67893
print('%0.2f' % test54_float)
print(round(test54_float, 2))

# 55 求三个方法打印结果

# 56 列出常见的状态码和意义

# 57 分别从前端、后端、数据库阐述web项目的性能优化
print('57 分别从前端、后端、数据库阐述web项目的性能优化')

# 58 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
print('58 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}')
test58_dic1 = {"name": "zs", "age": 18, "sex": "woman", "height": "170"}
test58_dic1.pop('age')
print(test58_dic1)
del test58_dic1["sex"]
print(test58_dic1)

# 59 列出常见MYSQL数据存储引擎
print('59 列出常见MYSQL数据存储引擎')

# 60 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
print('60 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]')

# 61 简述同源策略
print('61 简述同源策略')
print('协议相同(http https),域名相同，端口相同')

# 62 简述 cookie和session的区别
print('62 简述 cookie和session的区别')

# 63 简述多线程，多进程
print('63 简述多线程，多进程')

# 64 简述any()和all()方法
print('64 简述any()和all()方法')
print('any() 迭代器中有一个为真，即为真')
print('all() 迭代器中全为真，即为真')

# 65 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
print('65 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常')
print(
    'IOError:输入输出异常', '\r\n',
    'AttributeError:访问对象一个不存在的属性', '\r\n',
    'ImportError:无法引入模块或者包，基本都是路径问题', '\r\n',
    'IndentationError:语法错误，代码没有正确对齐', '\r\n',
    'IndexError:下标索引超出限制', '\r\n',
    'KeyError:视图访问字典中不存在的键', '\r\n',
    'SyntaxError:Python代码逻辑语法出错，不能执行', '\r\n',
    'NameError：使用了一个还未赋值的对象变量')

# 66 python copy 和 deepcopy的区别
print('66 python copy 和 deepcopy的区别')
print('copy:浅复制，引用数据复制的是引用地址')
print('deepcopy：深复制，引用数据直接赋值数据本身')

# 67 列出几种魔法方法并简要介绍用途
print('67 列出几种魔法方法并简要介绍用途')
print('__new__')
print('__init(self)__')
print('__class__  获取已知对象的类')
print('__str__ 将对象转换成字符串')
print('__del__ 对象调用结束以后，垃圾回收调用该魔法函数，来释放资源')
print('__hash__ 返回哈希值')

# 68

# 69 请将[i for i in range(3)] 改成生成器
print('69 请将[i for i in range(3)] 改成生成器')
test69_iter2 = (i for i in range(10))
print(type(test69_iter2))
print(test69_iter2.__next__())
print(next(test69_iter2))
for x in test69_iter2:
    print(x)

print(list(i for i in range(10)))
print(tuple(i for i in range(10)))

# 70 a = " hehheh ",去除首尾空格
print('70 a = " hehheh ",去除首尾空格')
test70_str1 = " hehheh "
print(test70_str1.strip())

# 71 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
print('71 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]')
test71_list1 = [0, -1, 3, -10, 5, 9]
test71_list2 = sorted(test71_list1)
print(test71_list1, test71_list2)

test71_list1.sort()
print(test71_list1)

# 72 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
print('72 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序')
test72_list1 = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
test72_gen1 = sorted(test72_list1, key=lambda x: x)
print(test72_gen1)

# 73 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为 [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
print('73 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为 [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小')
test73_list1 = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
test73_gen1 = sorted(test73_list1, key=lambda x: (x < 0, abs(x)))
print(test73_gen1)
test73_gen2 = sorted(test73_list1, key=lambda x: abs(x))
print(test73_gen2)

# 74 列表嵌套字典的排序，分别根据年龄和姓名排序
print('74 列表嵌套字典的排序，分别根据年龄和姓名排序')
test74_list1 = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54}, {"name": "wa", "age": 17},
                {"name": "df", "age": 23}]

test74_gen1 = sorted(test74_list1, key=lambda x: x["name"])
test74_gen2 = sorted(test74_list1, key=lambda x: x["age"])
print(test74_gen1)
print(test74_gen2)

# 75 列表嵌套元组，分别按字母和数字排序
print('75 列表嵌套元组，分别按字母和数字排序')
test75_tuple1 = [('sz', 13), ('ab', 24), ('ed', 56), ('hi', 12)]
test75_gen1 = sorted(test75_tuple1, key=lambda x: x[0], reverse=True)
test75_gen2 = sorted(test75_tuple1, key=lambda x: x[1], reverse=True)
print(test75_gen1)
print(test75_gen2)

# 76 列表嵌套列表排序，年龄数字相同怎么办？
print('76 列表嵌套列表排序，年龄数字相同怎么办？')
test76_list1 = [('sz', 13), ('ab', 24), ('ed', 56), ('hi', 12), ('hr', 24), ('as', 24), ]
# 只针对数字排序
test76_gen1 = sorted(test76_list1, key=lambda x: (x[1]))
# 针对数字排序，相同的时候，再针对字母排序
test76_gen2 = sorted(test76_list1, key=lambda x: (x[1], x[0]))
print(test76_gen1)
print(test76_gen2)

# 77 根据键对字典排序(方法1，zip函数)
print('77 根据键对字典排序(方法1，zip函数)')
test77_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
test77_list1 = zip(test77_dict1.keys(), test77_dict1.values())
test77_gen1 = sorted(test77_list1, key=lambda x: x[0])
test77_dict2 = {x[0]: x[1] for x in test77_gen1}
print(test77_dict2)

# 78 根据键对字典排序(方法2，不用zip函数)
print('78 根据键对字典排序(方法2，不用zip函数)')
test78_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
print(type(test78_dict1.items()), ':', test78_dict1.items())
# 老写法
# test78_list2 = [(x, y) for x, y in test78_dict1.items()]
# test78_gen1 = sorted(test78_list2, key=lambda x: x[0])
# 新写法 test78_dict1本来就是可迭代对象，不需要在转换为list
test78_gen1 = sorted(test78_dict1.items(), key=lambda x: x[0])
test78_dict2 = {x[0]: x[1] for x in test78_gen1}
print(test78_dict2)

# 79 列表推导式 字典推导式 生成器
print('79 列表推导式 字典推导式 生成器')
test79_list1 = [i for i in range(10)]
print('列表推导式', test79_list1)
test79_dic1 = {i: random.randint(11, 20) for i in range(1, 10)}
print('字典推导式', test79_dic1)
test79_gen1 = (i for i in range(10))
print('生成器', test79_gen1)
print('生成器具体的值', list(test79_gen1))

# 80 最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
print('80 最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用')
test80_list1 = ['ab', 'abc', 'a', 'jekg']
# 长度降序排序
test80_list2 = sorted(test80_list1, key=lambda x: len(x), reverse=True)
print(test80_list2)
test80_list1 = ['ab', 'abc', 'a', 'jekg']
test80_list1.sort(key=len, reverse=True)
print(test80_list1)

# 81 举例说明SQL注入和解决办法
print('81 举例说明SQL注入和解决办法')

# 82 s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']

# 83 正则匹配以http://163.com结尾的邮箱

# 84 递归求和
print('84 递归求和')


def deftest84(num):
    counts = 0
    if num == 1:
        return num
    else:
        counts = num + deftest84(num - 1)
    return counts


test84_int = deftest84(10)
print('递归求值', test84_int)

# 85 python字典和json字符串相互转化方法
print('85 python字典和json字符串相互转化方法')
import json

# 核心是json模块的 drmps 和 loads 函数功能
test85_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
test85_str1 = json.dumps(test85_dict1)
print('字典转字符串：', type(test85_str1), test85_str1)
test85_dict2 = json.loads(test85_str1)
print('字符串转字典：', type(test85_dict2), test85_dict2)

# 86 MyISAM 与 InnoDB 区别
print('86 MyISAM 与 InnoDB 区别')
# InnoDB支持事物，默认每一次执行，都包装成事物处理，更适合频繁涉及到修改的操作，安全性较高，支持外键。
# 自增长字段，必须只包含该字段
# 清空表时，是一行一行删除数据，效率比较慢

# 87 统计字符串中某字符出现次数
print('87 统计字符串中某字符出现次数')
test87_str1 = 'fsagbreyhefsdgbvhgrehsagbrfhetsagvedghre'

# str.counter可以统计某个字符出现的次数
print('a字符出现的次数：', test87_str1.count('a'))

# collections三方库可以统计所有字符出现的次数
test87_dict1 = collections.Counter(test87_str1)
print('每个字符出现的次数：', test87_dict1)

# 88 字符串转化大小写
print('88 字符串转化大小写')
test88_str1 = 'gegGEgeGERGH'
print('小写为:', test88_str1.lower())
print('大写为:', test88_str1.upper())

# 89 用两种方法去空格
print('89 用两种方法去空格')
test89_str1 = ' zhangsan  is  a       woman  '
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

# 32 用python删除文件和用linux命令删除文件方法
print('32 用python删除文件和用linux命令删除文件方法')
print(f'python方法：os.remove')
print(f'linux:rm')

# 33 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”
print('33 log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”')
import datetime

# strftime 时分秒(H M S)都要大写
test32_str1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(test32_str1)

# 33 数据库优化查询方法

# 34 请列出你会的任意一种统计图(条形图，折线图等)绘制的开源库，第三方也行
print('34 请列出你会的任意一种统计图(条形图，折线图等)绘制的开源库，第三方也行')
print('pyecharts', 'matplotlib')

# 35 写一段自定义异常代码
print('35 写一段自定义异常代码')


def def35():
    try:
        raise IndexError('测试测试')
    except IndexError as i:
        print(i)


def35()

# 36 正则表达式匹配中，(.*)和(.*?)匹配的区别？
print('36 正则表达式匹配中，(.*)和(.*?)匹配的区别？')
print('(.*) 是贪婪匹配，尽可能多的往后面匹配')
print('(.*？) 非贪婪匹配，尽可能少的匹配')
import re

test36_str = '<a>哈哈</a><a>呵呵</a>'
test36_re1 = re.findall("<a>(.*)</a>", test36_str)
test36_re2 = re.findall("<a>(.*?)</a>", test36_str)
print(test36_re1)
print(test36_re2)

# 38 简述Django的orm
print('38 简述Django的orm')
print('后续补充')

# 39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]
print('39 [[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]')
test39_list1 = [[1, 2], [3, 4], [5, 6]]
# 使用列表推导式 for i in a
test39_list2 = [j for i in test39_list1 for j in i]
print(test39_list2)

# 40 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果
print('40 x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果')
test40_str1 = 'abc'
test40_str2 = 'def'
test40_list1 = ['d', 'e', 'f']
print(test40_str1.join(test40_str2))
test40_str1 = 'abc'
test40_str2 = 'def'
test40_list1 = ['d', 'e', 'f']
print(test40_str1.join(test40_list1))

# 41 举例说明异常模块中try except else finally的相关意义
print('41 举例说明异常模块中try except else finally的相关意义')

# 42 python中交换两个数值
print('42 python中交换两个数值')
test42_i1, test42_i2 = 3, 4
print(test42_i1, test42_i2)
test42_i1, test42_i2 = test42_i2, test42_i1
print(test42_i1, test42_i2)

# 43 举例说明zip（）函数用法
print('43 举例说明zip（）函数用法')
test43_list1 = [1, 2, 3, 4, 5]
test43_list2 = ['a', 'b', 'c', 'd', 'e']
test43_res1 = zip(test43_list1, test43_list2)
print(list(test43_res1))

# 44 a="张明 98分"，用re.sub，将98替换为100
print('44 a="张明 98分"，用re.sub，将98替换为100')
test44_str1 = "张明 98分"

# 45 写5条常用sql语句

# 46 a="hello"和b="你好"编码成bytes类型
print('46 a="hello"和b="你好"编码成bytes类型')
test46_str1 = "hello"
test46_str2 = "你好"
print(test46_str1.encode())
print(test46_str2.encode(encoding='utf-8'))

# 47 [1,2,3]+[4,5,6]的结果是多少？
print('47 [1,2,3]+[4,5,6]的结果是多少？')
test47_list1 = [1, 2, 3]
test47_list2 = [4, 5, 6]
# +与extend相同
print(test47_list1 + test47_list2)
test47_list1.extend(test47_list2)
print(test47_list1)

# 48 提高python运行效率的方法
print('48 提高python运行效率的方法')
print(r'使用生成器，节约内存')
print(r'循环代码优化，避免过多重复代码')
print(r'多线程，多进程，协程')
print(r'多个判断，命中率高的放到最前面')

# 49 简述mysql和redis区别
print('49 简述mysql和redis区别')
print('存储方式不一样，'
      'mysql是关系数据库，数据主要固化到磁盘中'
      'redis是以键值对存储的菲关系数据库，数据主要保存在内存中')

# 50 遇到bug如何处理

# 51 正则匹配，匹配日期2018-03-20

# 52 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]
print('52 list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]')
test52_list1 = [2, 3, 5, 4, 9, 6]
test52_set = set(test52_list1)
test52_list2 = list(test52_set)
print(test52_list2)

# 53 写一个单列模式
print('53 写一个单列模式')


class Cls53():
    _cls = None

    def __new__(cls, *args, **kwargs):
        if not cls._cls:
            _cls = super().__new__(cls)
        return cls._cls


test53_t1 = Cls53()
test53_t2 = Cls53()
print(id(test53_t1))
print(id(test53_t2))

# 54 保留两位小数
test54_float = 3.67893
print('%0.2f' % test54_float)
print(round(test54_float, 2))

# 55 求三个方法打印结果

# 56 列出常见的状态码和意义

# 57 分别从前端、后端、数据库阐述web项目的性能优化
print('57 分别从前端、后端、数据库阐述web项目的性能优化')

# 58 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}
print('58 使用pop和del删除字典中的"name"字段，dic={"name":"zs","age":18}')
test58_dic1 = {"name": "zs", "age": 18, "sex": "woman", "height": "170"}
test58_dic1.pop('age')
print(test58_dic1)
del test58_dic1["sex"]
print(test58_dic1)

# 59 列出常见MYSQL数据存储引擎
print('59 列出常见MYSQL数据存储引擎')

# 60 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]
print('60 计算代码运行结果，zip函数历史文章已经说了，得出[("a",1),("b",2)，("c",3),("d",4),("e",5)]')

# 61 简述同源策略
print('61 简述同源策略')
print('协议相同(http https),域名相同，端口相同')

# 62 简述 cookie和session的区别
print('62 简述 cookie和session的区别')

# 63 简述多线程，多进程
print('63 简述多线程，多进程')

# 64 简述any()和all()方法
print('64 简述any()和all()方法')
print('any() 迭代器中有一个为真，即为真')
print('all() 迭代器中全为真，即为真')

# 65 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常
print('65 IOError、AttributeError、ImportError、IndentationError、IndexError、KeyError、SyntaxError、NameError分别代表什么异常')
print(
    'IOError:输入输出异常', '\r\n',
    'AttributeError:访问对象一个不存在的属性', '\r\n',
    'ImportError:无法引入模块或者包，基本都是路径问题', '\r\n',
    'IndentationError:语法错误，代码没有正确对齐', '\r\n',
    'IndexError:下标索引超出限制', '\r\n',
    'KeyError:视图访问字典中不存在的键', '\r\n',
    'SyntaxError:Python代码逻辑语法出错，不能执行', '\r\n',
    'NameError：使用了一个还未赋值的对象变量')

# 66 python copy 和 deepcopy的区别
print('66 python copy 和 deepcopy的区别')
print('copy:浅复制，引用数据复制的是引用地址')
print('deepcopy：深复制，引用数据直接赋值数据本身')

# 67 列出几种魔法方法并简要介绍用途
print('67 列出几种魔法方法并简要介绍用途')
print('__new__')
print('__init(self)__')
print('__class__  获取已知对象的类')
print('__str__ 将对象转换成字符串')
print('__del__ 对象调用结束以后，垃圾回收调用该魔法函数，来释放资源')
print('__hash__ 返回哈希值')

# 68

# 69 请将[i for i in range(3)] 改成生成器
print('69 请将[i for i in range(3)] 改成生成器')
test69_iter2 = (i for i in range(10))
print(type(test69_iter2))
print(test69_iter2.__next__())
print(next(test69_iter2))
for x in test69_iter2:
    print(x)

print(list(i for i in range(10)))
print(tuple(i for i in range(10)))

# 70 a = " hehheh ",去除首尾空格
print('70 a = " hehheh ",去除首尾空格')
test70_str1 = " hehheh "
print(test70_str1.strip())

# 71 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]
print('71 举例sort和sorted对列表排序，list=[0,-1,3,-10,5,9]')
test71_list1 = [0, -1, 3, -10, 5, 9]
test71_list2 = sorted(test71_list1)
print(test71_list1, test71_list2)

test71_list1.sort()
print(test71_list1)

# 72 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序
print('72 对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4],使用lambda函数从小到大排序')
test72_list1 = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
test72_gen1 = sorted(test72_list1, key=lambda x: x)
print(test72_gen1)

# 73 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为 [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小
print('73 使用lambda函数对list排序foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]，输出结果为 [0,2,4,8,8,9,-2,-4,-4,-5,-20]，正数从小到大，负数从大到小')
test73_list1 = [-5, 8, 0, 4, 9, -4, -20, -2, 8, 2, -4]
test73_gen1 = sorted(test73_list1, key=lambda x: (x < 0, abs(x)))
print(test73_gen1)
test73_gen2 = sorted(test73_list1, key=lambda x: abs(x))
print(test73_gen2)

# 74 列表嵌套字典的排序，分别根据年龄和姓名排序
print('74 列表嵌套字典的排序，分别根据年龄和姓名排序')
test74_list1 = [{"name": "zs", "age": 19}, {"name": "ll", "age": 54}, {"name": "wa", "age": 17},
                {"name": "df", "age": 23}]

test74_gen1 = sorted(test74_list1, key=lambda x: x["name"])
test74_gen2 = sorted(test74_list1, key=lambda x: x["age"])
print(test74_gen1)
print(test74_gen2)

# 75 列表嵌套元组，分别按字母和数字排序
print('75 列表嵌套元组，分别按字母和数字排序')
test75_tuple1 = [('sz', 13), ('ab', 24), ('ed', 56), ('hi', 12)]
test75_gen1 = sorted(test75_tuple1, key=lambda x: x[0], reverse=True)
test75_gen2 = sorted(test75_tuple1, key=lambda x: x[1], reverse=True)
print(test75_gen1)
print(test75_gen2)

# 76 列表嵌套列表排序，年龄数字相同怎么办？
print('76 列表嵌套列表排序，年龄数字相同怎么办？')
test76_list1 = [('sz', 13), ('ab', 24), ('ed', 56), ('hi', 12), ('hr', 24), ('as', 24), ]
# 只针对数字排序
test76_gen1 = sorted(test76_list1, key=lambda x: (x[1]))
# 针对数字排序，相同的时候，再针对字母排序
test76_gen2 = sorted(test76_list1, key=lambda x: (x[1], x[0]))
print(test76_gen1)
print(test76_gen2)

# 77 根据键对字典排序(方法1，zip函数)
print('77 根据键对字典排序(方法1，zip函数)')
test77_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
test77_list1 = zip(test77_dict1.keys(), test77_dict1.values())
test77_gen1 = sorted(test77_list1, key=lambda x: x[0])
test77_dict2 = {x[0]: x[1] for x in test77_gen1}
print(test77_dict2)

# 78 根据键对字典排序(方法2，不用zip函数)
print('78 根据键对字典排序(方法2，不用zip函数)')
test78_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
print(type(test78_dict1.items()), ':', test78_dict1.items())
# 老写法
# test78_list2 = [(x, y) for x, y in test78_dict1.items()]
# test78_gen1 = sorted(test78_list2, key=lambda x: x[0])
# 新写法 test78_dict1本来就是可迭代对象，不需要在转换为list
test78_gen1 = sorted(test78_dict1.items(), key=lambda x: x[0])
test78_dict2 = {x[0]: x[1] for x in test78_gen1}
print(test78_dict2)

# 79 列表推导式 字典推导式 生成器
print('79 列表推导式 字典推导式 生成器')
test79_list1 = [i for i in range(10)]
print('列表推导式', test79_list1)
test79_dic1 = {i: random.randint(11, 20) for i in range(1, 10)}
print('字典推导式', test79_dic1)
test79_gen1 = (i for i in range(10))
print('生成器', test79_gen1)
print('生成器具体的值', list(test79_gen1))

# 80 最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用
print('80 最后出一道检验题目，根据字符串长度排序，看排序是否灵活运用')
test80_list1 = ['ab', 'abc', 'a', 'jekg']
# 长度降序排序
test80_list2 = sorted(test80_list1, key=lambda x: len(x), reverse=True)
print(test80_list2)
test80_list1 = ['ab', 'abc', 'a', 'jekg']
test80_list1.sort(key=len, reverse=True)
print(test80_list1)

# 81 举例说明SQL注入和解决办法
print('81 举例说明SQL注入和解决办法')

# 82 s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']

# 83 正则匹配以http://163.com结尾的邮箱

# 84 递归求和
print('84 递归求和')


def deftest84(num):
    counts = 0
    if num == 1:
        return num
    else:
        counts = num + deftest84(num - 1)
    return counts


test84_int = deftest84(10)
print('递归求值', test84_int)

# 85 python字典和json字符串相互转化方法
print('85 python字典和json字符串相互转化方法')
import json

# 核心是json模块的 drmps 和 loads 函数功能
test85_dict1 = {'name': 'zhangsan', 'sex': 'man', 'city': 'bj'}
test85_str1 = json.dumps(test85_dict1)
print('字典转字符串：', type(test85_str1), test85_str1)
test85_dict2 = json.loads(test85_str1)
print('字符串转字典：', type(test85_dict2), test85_dict2)

# 86 MyISAM 与 InnoDB 区别
print('86 MyISAM 与 InnoDB 区别')
# InnoDB支持事物，默认每一次执行，都包装成事物处理，更适合频繁涉及到修改的操作，安全性较高，支持外键。
# 自增长字段，必须只包含该字段
# 清空表时，是一行一行删除数据，效率比较慢

# 87 统计字符串中某字符出现次数
print('87 统计字符串中某字符出现次数')
test87_str1 = 'fsagbreyhefsdgbvhgrehsagbrfhetsagvedghre'

# str.counter可以统计某个字符出现的次数
print('a字符出现的次数：', test87_str1.count('a'))

# collections三方库可以统计所有字符出现的次数
test87_dict1 = collections.Counter(test87_str1)
print('每个字符出现的次数：', test87_dict1)

# 88 字符串转化大小写
print('88 字符串转化大小写')
test88_str1 = 'gegGEgeGERGH'
print('小写为:', test88_str1.lower())
print('大写为:', test88_str1.upper())

# 89 用两种方法去空格
print('89 用两种方法去空格')
test89_str1 = ' zhangsan  is  a       woman  '
test89_str2 = re.sub(r" +", ' ', test89_str1)
print('正则替换：', '"' + test89_str2.strip() + '"')
test89_list1 = test89_str1.split(' ')
test89_str3 = ''.join(test89_list1)
print('分隔替换：', '"' + test89_str3 + '"')

# 90

# 91 简述python引用计数机制
print('91 简述python引用计数机制')


class Cls91():
    def __init__(self, name):
        self.name = name

    # 当类的示例引用为0时，才真的执行实例的删除操作，以及垃圾回收机制
    def __del__(self):
        print('执行了删除操作')


cls91_1 = Cls91('测试')
cls91_2 = cls91_1
cls91_3 = cls91_1
print(id(cls91_1), id(cls91_2), id(cls91_3))
print('开始删除2')
del (cls91_2)
print('开始删除1')
del (cls91_1)
print('开始删除3')
del (cls91_3)
print('删除完成')

# 92 int("1.4"),int(1.4)输出结果？
print('92 int("1.4"),int(1.4)输出结果？')
# print(int('1.4'))
print(int(1.4))
print(int(1.6))

# 93 列举3条以上PEP8编码规范

# 94 正则表达式匹配第一个URL

# 95  正则匹配中文

# 96 简述乐观锁和悲观锁
print('96 简述乐观锁和悲观锁')
# 乐观锁：基于查询大于更新的基准，增加一个递增变量，每次读取先读取递增变量，重新更新的时候，判断递增变量是否与之前查询到的一致，才更新
# 悲观锁：悲观态度，认为更新很容易出错，每次执行前，都加锁，只能同时一个操作操作数据

# 97 r、r+、rb、rb+文件打开模式区别
print('97 r、r+、rb、rb+文件打开模式区别')
print('r 只读模式打开')
print('w 写入模式打开')
print('rw 读写模式打开')
print('rb 字节流格式打开')
print('a 追加模式打开')
print('*+ 上述模式全部增加+,则变为读写模式')

# 98 Linux命令重定向> 和 >>
print('98 Linux命令重定向> 和 >>')
print('> 表示输出到哪里，会覆盖原有文件')
print('>> 表示追加，会追加到原有文件的末尾')

# 99 正则

# 100 Python 传参数是传值还是传地址？
print('100 Python 传参数是传值还是传地址？')
# python 以传递地址的方式进行参数传递
# 如果是不可变类型(数字，字符串，元组)应为变量不可修改，所以直接传递变量的地址
# 如果是可变类型，直接传入参数地址更有效

# 101 求两个列表的交集、差集、并集
print('101 求两个列表的交集、差集、并集')
test101_list1 = [1, 2, 3, 4, 5, 6]
test101_list2 = [2, 4, 6, 7, 9, 78]
# 有两种方式
# 第一种是用set的集合运算法
# 第二种方式为set集合的方法
# 方式一 &:交集 |:并集 -:差集
print('交集：', list(set(test101_list1) & set(test101_list2)))
print('并集：', list(set(test101_list1) | set(test101_list2)))
print('差集：', list(set(test101_list1) - set(test101_list2)))

print('方法二')
print('交集：', list(set(test101_list1).intersection(set(test101_list2))))
print('并集：', list(set(test101_list1).union(set(test101_list2))))
print('差集：', list(set(test101_list1).difference(set(test101_list2))))

# 102 生成0-100的随机数
print('102 生成0-100的随机数')
print(int(random.random() * 100))
print(random.randint(0, 101))

# 103 lambda匿名函数的好处
print('103 lambda匿名函数的好处')
print('精简代码，省去了定义函数，省去了for循环')

# 104 常见的网络传输协议
print('104 常见的网络传输协议')
test104_list = ['http', 'https', 'tcp', 'udp', 'ftp']
print('常见的网络传输协议', test104_list)

#105 单引号，双引号，三引号的用法
print('105 单引号，双引号，三引号的用法')
print('单引号和双引号使用没有差别')
print('三引号通常直接书写多行，通常用于大段文字')

#106 python垃圾回收机制
print('106 python垃圾回收机制')
print('python 垃圾回收机制，主要运用引用为0的操作，当一个对象的引用为0是，执行删除该引用对用的实体并回收操作')

#107

#108 python中读取Excel文件的方法
print('108 python中读取Excel文件的方法')
print('应用pandas库')

#109 简述多线程 多进程

#110 python正则中search和match

