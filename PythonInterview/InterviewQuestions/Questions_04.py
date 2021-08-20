"""
语言概念与机制
http://coolpython.net/python_interview/basic/py_concept_mechanism.html
"""
# 01 谈下GIL 全局解释器锁

# 02 遍历文件夹，输出文件夹下所有文件的路径
import os


def print_directory_contents(path):
    test02_dirList = os.listdir(path)
    for childfile in test02_dirList:
        childPath = os.path.join(path, childfile)
        # 判断为文件夹
        if os.path.isdir(childPath):
            print_directory_contents(childPath)
        else:
            print(childPath)


print_directory_contents('./')


def get_english_score():
    return 90


def get_history_score():
    return 95


def get_score(course):
    golbal_dic = globals()
    print(golbal_dic)
    funname = f'get_{course}_score'
    # 如果找不到，直接返回lambda表达式，不会应为程序而报错
    func = golbal_dic.get(funname, lambda: 0)
    return func()


print(get_score('english'))
print(get_score('abc'))

for i, j in enumerate([3, 65, 2, 5, 6]):
    print(i, j)


def abc():
    print('aa')


print(abc())

import enum

