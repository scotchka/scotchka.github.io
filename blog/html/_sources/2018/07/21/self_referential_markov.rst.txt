Self-referential data structures
================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

Most data structures in Python can hold arbitrary heterogenous data. This is because
the underlying C structures contain pointers to other locations in memory. For example,
a Python list is implemented in C as an array of pointers.

A perhaps startling consequence is that a mutable data structure - such as a list - can
contain itself as an element:

>>> lst = [1, 2, 3]
>>> lst.append(lst)
>>> lst
[1, 2, 3, [...]]
>>> lst[-1] is lst
True

A self-referential data structure, though somewhat obscure, can be more compact.
As a use case, let's consider the familiar exercise of a Markov chain text generator.

Given a string, we construct a list of consecutive pairs - or bigrams - of words that appear. For
each unique bigram, its second word may be the first word in multiple other bigrams. We
randomly choose one such bigram, and repeat the process. The sequence of words encountered
in this random series of jumps through the text constitutes the Markov text.

First, we define a function to make a data structure that allows for random traversal:

.. literalinclude:: markov.py
    :pyobject: make_chain

``chain`` is self-referential because the ``append`` method, which adds to a list inside
``chain``, takes as argument a component of ``chain`` itself. We can gain more insight with
a small example:

..
	>>> from random import seed
	>>> seed(42)

	>>> from markov import make_chain, make_text

>>> chain = make_chain('a a a b')
>>> bigram = ('a', 'a')
>>> link = chain[bigram]
>>> link
{('a', 'a'): [{...}, {('a', 'b'): [{('b', 'a'): [{...}]}]}]}
>>> link[bigram][0] is link
True

``link`` is a dictionary of one key-value pair. The key is a bigram, and the value is a list
of dictionaries, each having the same structure as ``link``. Though the structure is finite,
we can "descend" into it indefinitely. This suggests a simple strategy for random traversal:

.. literalinclude:: markov.py
    :pyobject: make_text

Let's generate a random text based on a famous work of literature:

.. code-block:: default

	>>> s = """
	... Beautiful is better than ugly.
	... Explicit is better than implicit.
	... Simple is better than complex.
	... Complex is better than complicated.
	... Flat is better than nested.
	... Sparse is better than dense."""

	>>> chain = make_chain(s)
	>>> make_text(chain)
	'than ugly. Explicit is better than implicit. Simple is better than ugly. Explicit is better than nested. Sparse is better than complicated. '

To be sure, compared to the usual implementations of Markov text generation, this version
is quite inscrutable. It is to be taken as a proof of principle. You should almost always
avoid self-referential data structures in production code!
