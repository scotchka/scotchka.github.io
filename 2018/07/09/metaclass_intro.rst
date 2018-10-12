Metaclasses made simple
=======================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

You probably have added the ``__repr__`` method to a Python class:

.. literalinclude:: meta_cats.py
    :pyobject: Cat

This gives a customized representation to the instance at the command line:

..
	>>> from meta_cats import Cat, FancyCat, MetaCat

>>> Cat()
<😻>

However, this ``__repr__`` has no effect on the class itself:

>>> Cat
<class 'meta_cats.Cat'>

The reason is that a method defined on a class acts on instances of the class but not
the class itself. But what if the class is itself an instance? An instance of what class?
Python provides an easy way to find out:

>>> type(Cat)
<class 'type'>

So we see that a class is an instance of the built-in class ``type``. This means that we
should be able to subclass ``type``, add methods to it, and instantiate classes using
our customized type. Here is a small example:

.. literalinclude:: meta_cats.py
    :pyobject: MetaCat

Note that ``MetaCat`` descends from ``type`` and has a ``__repr__`` method that has a parameter
``cls``. This is to emphasize that instances of ``MetaCat`` are themselves classes.

We can instantiate a class in the usual way, except for an additional optional parameter.

.. literalinclude:: meta_cats.py
    :pyobject: FancyCat

The ``metaclass`` parameter in the class definition instructs Python to make an instance of ``MetaCat``
instead of ``type``. Let's verify this:

>>> type(FancyCat) is MetaCat
True

Finally, let's see what happens when we evaluate the class ``FancyCat`` on the Python command line:

>>> FancyCat
<class 😻>

Indeed, the ``__repr__`` method defined on ``MetaCat`` is called, and returns a customized representaion.

To summarize, every class in Python is an instance of some class, often referred to as a metaclass to
distinguish it from other classes. ``type`` is the built-in metaclass of which ``int``, ``dict``, and your own
classes are instances. And just like with most classes, you can subclass ``type`` to make custom metaclasses,
analogous to subclassing ``object`` to make custom classes.
