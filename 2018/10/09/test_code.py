"""
>>> def inc():
...     return x + 1

>>> type(inc)
<class 'function'>

>>> Function = type(inc)
>>> another_inc = Function(inc.__code__, {'x': 2})
>>> another_inc()
3

>>> import re
>>> from re import match
>>> match.__globals__ is re.__dict__
True

>>> Module = type(re)
>>> mod = Module('another module')
>>> dir(mod)
['__doc__', '__loader__', '__name__', '__package__', '__spec__']

>>> mod.x = 42
>>> another_inc.__globals__.update(mod.__dict__)
>>> another_inc()
43

"""