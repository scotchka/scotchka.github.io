Instantiating functions and modules
===================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

In Python, anything that you can assign to a variable is an object, including a function.

.. code-block:: default

	>>> def inc():
	...     return x + 1

	>>> type(inc)
	<class 'function'>

Normally, Python creates a function object upon function definition, but we can also
instantiate a function like other objects - by calling its class:

>>> Function = type(inc)
>>> another_inc = Function(inc.__code__, {'x': 2})
>>> another_inc()
3

The class ``Function`` takes two required arguments. First, a code object which is a data
structure containing compiled bytecode. Second, a dictionary that is the global scope
of the resulting function. Indeed, calling the original ``inc`` would raise an error since
``x`` is not defined, but ``another_inc`` works because its global scope does have ``x``.

More generally, the global scope of a function is the module that contains it. Let's confirm
this with a function from a standard module:

>>> import re
>>> from re import match
>>> match.__globals__ is re.__dict__
True

A module is a simple object whose main purpose is to hold objects that belong to it - in
other words, provide a namespace. It turns out that we can also dynamically instantiate a
module:

>>> Module = type(re)
>>> mod = Module('another module')
>>> dir(mod)
['__doc__', '__loader__', '__name__', '__package__', '__spec__']

Finally, we change the global scope of our existing function to the new module:

>>> mod.x = 42
>>> another_inc.__globals__.update(mod.__dict__)
>>> another_inc()
43
