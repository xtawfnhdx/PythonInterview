import traceback


def abc():
    try:
        print("try in ")
        # s=2/0
        raise Exception("abc is test error")
    except ZeroDivisionError:
        print('except1 in')
    except Exception:
        print('except2 in')
    else:
        print("else in")


def Throwabc():
    raise Exception("this is a error")


abc()


class MytestError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def test_myerror():
    try:
        raise MytestError("this is a error")
    except MytestError as e:
        # 输出堆栈信息
        traceback.print_exc()
        print(e)


test_myerror()
