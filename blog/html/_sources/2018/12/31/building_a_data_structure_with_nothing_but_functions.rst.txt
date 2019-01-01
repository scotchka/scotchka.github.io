Building a data structure with nothing but functions
====================================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::


A simple but far reaching consequence of being able to nest functions is that
data can be stored in the enclosing scope  - or closure - of
the inner function. Consider the following function:

.. literalinclude:: stack_functions.py
    :pyobject: make_node

When ``make_node`` is called with two arguments, they are attached to the closure
of the returned function. Subsequently, we can access the two arguments via

.. literalinclude:: stack_functions.py
    :pyobject: value

and

.. literalinclude:: stack_functions.py
    :pyobject: next_node

..
    >>> from stack_functions import make_node, value, next_node

For example,

>>> node = make_node("head", "tail")
>>> value(node)
'head'
>>> next_node(node)
'tail'

With these functions in hand, it is easy to implement a stack as a linked list.
We define the usual stack operations

.. literalinclude:: stack_functions.py
    :pyobject: push

and

.. literalinclude:: stack_functions.py
    :pyobject: pop

..
    >>> from stack_functions import push, pop

The behavior is as expected:

>>> stack = None
>>> stack = push(1, stack)
>>> stack = push(2, stack)
>>> stack = push(3, stack)
>>> val, stack = pop(stack)
>>> val
3
>>> val, stack = pop(stack)
>>> val
2
>>> val, stack = pop(stack)
>>> val
1

It is remarkable that this stack does not use any built-in data structure such as an array, nor does it
build the linked list by instantiating node objects. Rather, there is a chain of functions wherein each
function's closure contains a value and a reference to the next function.

This discussion was inspired by the classic
`Structure and Interpretation of Computer Programs <https://mitpress.mit.edu/sites/default/files/sicp/index.html>`_.
In particular, section 2.1 introduces the notion of using closures to build data structures.
