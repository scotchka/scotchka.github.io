Instantiating functions and modules
===================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

In Python, anything that you can assign to a variable is an object, including a function.

.. literalinclude:: test_code.txt
    :lines: 2-6

Normally, Python creates a function object upon function definition, but we can also
instantiate a function like other objects - by calling its class:

.. literalinclude:: test_code.txt
    :lines: 8-11

The class ``Function`` takes two required arguments. First, a code object which is a data
structure containing compiled bytecode. Second, a dictionary that is the global scope
of the resulting function. Indeed, calling the original ``inc`` would raise an error since
``x`` is not defined, but ``another_inc`` works because its global scope does have ``x``.

More generally, the global scope of a function is the module that contains it. Let's confirm
this with a function from a standard module:

.. literalinclude:: test_code.txt
    :lines: 13-16

A module is a simple object whose main purpose is to hold objects that belong to it - in
other words, provide a namespace. It turns out that we can also dynamically instantiate a
module:

.. literalinclude:: test_code.txt
    :lines: 18-21

Finally, we change the global scope of our existing function to the new module:

.. literalinclude:: test_code.txt
    :lines: 23-26
