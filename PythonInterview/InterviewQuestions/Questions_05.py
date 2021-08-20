import enum
import hashlib


# 01 枚举使用
# 装饰器，保证枚举内容不重复
@enum.unique
class Color(enum.Enum):
    Red = 1
    Blue = 2
    Yellow = 3


def getColor(color):
    if color == Color.Red.value:
        print('红色')
    elif color == Color.Blue.value:
        print('蓝色')
    elif color == Color.Yellow.value:
        print('黄色')
    else:
        print('其他颜色')


getColor(1)
getColor(2)
getColor(3)
getColor(4)

# md5 散列使用
test02_str1 = "abcdefg"
test02_byte = str.encode(test02_str1, encoding='utf-8')
print(type(test02_byte))
m = hashlib.md5()
m.update(test02_byte)
test02_md5 = m.hexdigest()
print(f'{test02_str1} 散列以后的数据为 {test02_md5}')


# 03 验证代码静态检查
class Test03Stu():
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def printstr(self):
        print(f'name:{self.name},age:{self.age}')
test03_1=Test03Stu('张三',16.5)
test03_2=Test03Stu('李四','17')
test03_1.printstr()
test03_2.printstr()
