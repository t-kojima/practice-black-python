"""
Monkey Patch（オープンクラス）
"""


class Container(object):
    pass


c = Container()


def new_method(self, val):
    return val


# インスタンスでは無くクラスに追加している点注意
Container.new_method = new_method
ret = c.new_method('new!')

print(ret)
