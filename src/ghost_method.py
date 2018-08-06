class DynamicProxy(object):
    def __init__(self, value):
        self._value = value

    def __getattr__(self, name):
        """
        __getattr__ (rubyでのmethod_missing)
        実装されていないメソッドが呼ばれた時、呼び出される
        name引数にはその時のメソッド名が入る
        """
        return getattr(self._value, name)


proc = DynamicProxy('hoge')
print(proc.title())

"""
- DynamicProxy#titleは存在しないメソッドなので、DynamicProxy#__getattr__が呼ばれる
- getattrで対象オブジェクト（ここでは'hoge'）のname(title)メソッドが呼ばれる
- 'hoge'.title()が処理され、結果の'Hoge'が返る。
"""
