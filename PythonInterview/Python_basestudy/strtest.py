s1='''
这是
一行
文本
'''
print(s1)

print(len(s1))
print(s1[4])
s2=['a','ab','cc']
print('_'.join(s2))

print('字符串格式化')
print("%s,%s" %("zhangsan",12))

n1="{} is a boy,age={}".format("zhangsan",12)
print(n1)
n2="{1} is a girl,age={0}".format(13,"huahua")
print(n2)
n3="{a} is a {b} is b".format(a="aa",b="bb")
print(n3)

name='xiaowang'
age=13
print(f"{name} age is {age}")
