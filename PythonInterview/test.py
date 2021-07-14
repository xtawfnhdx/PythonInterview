name='a'
age='b'
print(f"{name} anme {age} ages")


va=lambda x,y:x+y
print(va(5,6))


def test1():
    if True:
        i = 1  # 局部变量i属于test1中的局部作用域范围

    # 访问i时，i存在于局部作用域中


    print(i)  # 输出1