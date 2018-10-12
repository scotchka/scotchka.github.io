A C style enum in Python
========================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::


The `enum <https://docs.python.org/3/library/enum.html#creating-an-enum>`_ standard module allows you to
make names whose values are arbitrary:

.. code-block:: python

    from enum import Enum
    class Color(Enum):
        RED = 0
        GREEN = 1
        BLUE = 2

It is convenient to use ``Color.RED`` in code because the compiler/interpreter will ensure against
typos, and sensibly chosen names will enhance readibility. However, unlike in C, Python's ``enum``
forces you to assign values. It would be nice if we can simply write

.. code-block:: python

    class Color(Enum):
        RED
        GREEN
        BLUE

and have the attributes autoincrement. It turns out that with a little metaprogramming, we can.

Python 3 introduced ``__prepare__``, which is a method on the metaclass invoked before class creation.
It by default returns a dictionary, which will contain the class attributes required for class creation.
For example, the statement ``RED = 1`` above has the effect of adding a key/value pair to this
dictionary: ``prepared_dict['RED'] = 1``.

The idea is to override ``__prepare__`` and return a customized dictonary that assigns each key the next
available integer. Here is an implementation of this dictionary:

.. literalinclude:: enum3.py
    :pyobject: AutoDict

Under a class definition, for each variable that appears in an expression - as opposed to the left hand side
of an assignment - Python will look up its value first in this dictionary, calling the ``__getitem__``
method, which in turn **assigns** to it the next integer.

Then we create a metaclass with a ``__prepare__`` method that returns an instance of ``AutoDict``,

.. literalinclude:: enum3.py
    :pyobject: EnumMeta

and a base class that instantiates ``EnumMeta``

.. literalinclude:: enum3.py
    :pyobject: Enum

Let's try running the example above:

.. literalinclude:: test_enum3.txt
    :lines: 4-16

So we have an enum class that automatically assign and increment values to its attributes.
