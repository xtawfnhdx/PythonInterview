"""
函数相关面试题
http://coolpython.net/python_interview/basic/function-interview.html
"""

# 01 fun(*args,**kwargs)中的args,*kwargs什么意思？
print('01 fun(*args,**kwargs)中的args,*kwargs什么意思？')
print('*args 一个或多个单字符参数，数据类型是元组 tuple ')
print('**kwargs 一个或多个字典参数， 数据类型是字典 dict')

# 02 说说你对lambda表达式的理解
print('02 说说你对lambda表达式的理解')
print('匿名表达式 创建一个没有名字的函数 自动返回结果')

# 03 python 传参数是传值还是传地址
print('03 python 传参数是传值还是传地址')
print('不可变数据，传地址')
print('可变对象，传地址')

# 05 说说你对装饰器的理解
print('05 说说你对装饰器的理解')
print('装饰器就是一些特殊功能的函数 将函数打包使用')
""" 
第一点：python中一切皆对象，函数也是对象
将函数作为参数传递到函数内部，从而执行参数函数
第二点：函数可以作为另一个函数的返回值
第三点：闭包 
"""

"""
数据类型相关面试题
"""

# 06 字典如何删除键和合并两个字典
print('06 字典如何删除键和合并两个字典')
test06_dict1 = {'name': 'zhangsan', 'age': 15, 'sex': 'woman'}
print(test06_dict1)
del test06_dict1['age']
print(test06_dict1)

test06_dict1['age'] = 18
print(test06_dict1)
# pop可以提供第二个参数，如果键不在，可以返回第二个参数
print(test06_dict1.pop('age'))
print(test06_dict1)

test06_dict2 = {'city': 'bj', 'country': 'zh'}
test06_dict1.update(test06_dict2)
print(test06_dict1)
test06_dict1 = {'name': 'zhangsan', 'age': 15, 'sex': 'woman'}
print({**test06_dict1, **test06_dict2})
print(dict(test06_dict1.items() | test06_dict2.items()))

#07 python 实现列表去重的方法
test07_list1=[1,2,4,3,9,7,4,3,6,7,3,2,5,7]
test07_set=set(test07_list1)
print(list(test07_set))

#08 a="hello"和b="你好" 编码成bytes类型
test08_str1='hello'
test08_str2="你好"
print(test08_str1.encode())
print(test08_str2.encode(encoding='utf-8'))

#09 python中列表和元组有什么区别
print('09 python中列表和元组有什么区别')
print('列表可变，元组不可变')
print('使用场景：函数返回多个值时，可以包装成元组，而非列表')
print('传入可变参数时，可变参数的类型是元组，保证传入参数无法修改，保证程序正确性')
print('元组可以作为字典的key ，可以存储到集合中')

#10 什么是负索引
print('正索引从左到右，从0开始')
print('负索引从右到左，从-1开始')

#11 字符串里输出转义字符
print(r'\r\n')

