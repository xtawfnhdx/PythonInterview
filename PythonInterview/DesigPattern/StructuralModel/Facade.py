"""
外观模式
"""
class OpenWindows():
    def open(self):
        print('开机')
    def close(self):
        print('关机')


class OpenWX():
    def open(self):
        print('打开微信')

    def close(self):
        print('关闭微信')


class OpenChrome():
    def open(self):
        print('打开浏览器')

    def close(self):
        print('关闭浏览器')

class Action():
    def __init__(self):
        self.Win=OpenWindows()
        self.WX=OpenWX()
        self.Ch=OpenChrome()
    def open(self):
        self.Win.open()
        self.WX.open()
        self.Ch.open()
    def close(self):
        self.Win.close()
        self.WX.close()
        self.Ch.close()

if __name__=='__main__':
    ac=Action()
    ac.open()
    ac.close()

