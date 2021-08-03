"""
适配器模式
"""

class XMLAction():
    def xmlexcute(self):
        print('XML Ececute')

class JsonAction():
    def jsonexecute(self):
        print('json execute')

class Adapter(XMLAction,JsonAction):
    def __init__(self,xmlstr:"xml字符串"):
        self.xmlstr=xmlstr
    def adapterFun(self):
        print('get xmlStr')
        self.xmlexcute()
        print('adapter to json')
        self.jsonexecute()
        print('execute end')

def client(tar:"输入一个xml字符串"):
    ad=Adapter(tar)
    ad.adapterFun()

if __name__=="__main__":
    client('<abx></abc>')