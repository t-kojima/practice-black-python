"""
高階関数
"""

from operator import methodcaller

"""
そもそもmethodcallerってなんなのさ
https://docs.python.jp/3/library/operator.html#operator.methodcaller
文字通りメソッドを呼び出すオブジェクトだった
f = methodcaller('name', 'arg1', 'arg2')とすると、f(b)でb.name('arg1', 'arg2')になる
"""


class NullSafeContainer(object):
    def __getattr__(self, name):
        def _(targ):
            if targ is None:
                return lambda *args, **kw: None
            return lambda *args, **kw: methodcaller(name, *args, **kw)(targ)
        return _


ns = NullSafeContainer()
ret = ns.replace('foo bar baz')('bar', 'gege')
"""
- ns.replace('foo bar baz') のタイミングで関数が返る。その関数の引数として'foo bar baz'が渡される(targ)
- targがあるとmethodcallerが呼ばれ、f = methodcaller('replace', 'bar', 'gege')となり
  f('foo bar baz')となる
- 結果、'foo bar baz'.replace('bar', 'gete')が呼ばれることとなる
"""
print(ret)

ret2 = ns.replace(None)('bar', 'gete')
"""
- targ == Noneの場合、Noneが返される
"""
print(ret2)
