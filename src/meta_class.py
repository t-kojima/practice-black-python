"""
Meta Class (クラスの動的な生成)
"""

MyClass = type('MyClass', (object,), {
    '__init__': lambda self, val: setattr(self, '_val', val),
    'say': lambda self: self._val, },
)

"""
以下と同義

class MyClass():
    def __init__(self, val):
        self._val = val

    def say(self):
        return self._val
"""

mc = MyClass('aaa')
print(mc.say())

"""
デコレータもどきのメタクラスサンプル
"""


def _logging_hook(func):
    def __(*args, **kw):
        print(f'before : {func.__name__}')
        ret = func(*args, **kw)
        print(f'after : {func.__name__}')
        return ret
    return __


from types import MethodType, FunctionType, LambdaType


class LoggingHookKlass(type):
    def __new__(cls, name, bases, dict):
        hooked_attrs = {
            k: _logging_hook(v) for k, v in dict.items() if isinstance(v, (MethodType, FunctionType, LambdaType))
        }
        return type.__new__(cls, name, bases, hooked_attrs)


"""
python2 では __metaclass__ = LoggingHookKlass
python3 では Ninja(metaclass=LoggingHookKlass)
"""


class Ninja(metaclass=LoggingHookKlass):
    # __metaclass__ = LoggingHookKlass

    def aisatsu(self, other):
        print(f'hello {other}')


ninja = Ninja()
ninja.aisatsu('hoge')
