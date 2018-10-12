Balance brackets with the call stack
====================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

A classic algorithm problem is to determine whether a string
containing some sequences of brackets (possibly of different types)
is balanced, that is, whether the string is a valid mathematical
expression. For example, ``()`` is balanced, and ``)(`` is not.

The typical solution involves iterating thru the string and maintaining
a stack - pushing an opening bracket onto the stack when encountered,
and popping it off when the corresponding closing bracket is seen.

But why not, instead of making our own stack, use the call stack? Python's
``inspect`` module allows us to do just that.

.. literalinclude:: balance_brackets.py
   :lines: 1

This module's ``stack`` function returns the call stack from top to bottom,
so the previous frame is ``stack()[1]``.

We define a function ``_stack`` that
iterates through a list of characters. Upon seeing an opening bracket, it pushes
onto the call stack by calling itself, and in case of a closing bracket, pops by
simply returning. By inspecting the previous frame, we ensure that the closing
bracket matches the most recent opening bracket, and that there are no opening
brackets left on the call stack at the end,

.. literalinclude:: balance_brackets.py
    :pyobject: _stack

where ``BRACKETS`` is a mapping of closing to opening brackets:

.. literalinclude:: balance_brackets.py
    :lines: 3

In the event of an unbalanced expression, ``_stack`` raises ``IndexError``,
hence we define ``is_balanced`` that wraps ``_stack`` inside of a try/except:

.. literalinclude:: balance_brackets.py
    :pyobject: is_balanced

Some test examples:

.. 
	>>> from balance_brackets import is_balanced

>>> is_balanced("[]")
True
>>> is_balanced(")(")
False
>>> is_balanced("{[}]")
False
>>> is_balanced("(")
False
