"""
变量相关面试题
http://coolpython.net/python_interview/basic/python-interview-variable.html
"""
# 01 python的内置数据类型都有哪些
print('01 python的内置数据类型都有哪些')
print('bytes', 'int', 'float', 'str', 'list', 'set', 'tuple', 'dict', 'bool')

# 02 如何在一个函数内部修改全局变量
print('02 如何在一个函数内部修改全局变量')
str = '在函数内部使用global 但如果是一个可变对象，直接修改即可'
print(str)

# 03 哪些是可变对象，哪些是不可变对象，他们的区别是什么
print('03 哪些是可变对象，哪些是不可变对象，他们的区别是什么')
print('不可变对象', 'int float str tuple')
print('可变对象', 'list dict set')
print('区别：充分理解可变对象与不可变对象，可变对象是指变量指向的地址不变，而地址指向的内容改变')
print('不可变对象是指指向地址的对应的值是不可变的，修改的仅仅是指向的地址')

# 04 简述python变量的作用域
print('04 简述python变量的作用域')
print('局部作用域：函数内部的作用域')
print('嵌套作用域：一个函数内部又定义了一个作用域，嵌套作用域是一个相对概念')
print('全局作用域：每个模块都是一个全局作用域')
print('内置作用域：系统中固定模块里定义的变量')

# 05 is和==的区别
print('05 is和==的区别')
print('is:身份运算符 判定一句是内存地址是否相同')
print('==:比较关系运算符 判定数据是否相等')
test05_list1 = [1]
test05_list2 = [1]
print(test05_list1 == test05_list2)
print(test05_list1 is test05_list2)
print('内存池概念：-5到256 python会认为这些小的数据经常会用到，所以启动时就会创建这些数据，已经存在了')

#06 连接字符串用join还是+
print('06 连接字符串用join还是+')
print('使用join 内存中开辟一块存储空间，避免反复创建字符串对象')

