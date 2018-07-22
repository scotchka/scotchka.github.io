'''
>>> lst = [1, 2, 3]
>>> lst.append(lst)
>>> lst
[1, 2, 3, [...]]
>>> lst[-1] is lst
True

>>> from random import seed
>>> seed(42)

>>> from markov import markov

>>> s = """
... Beautiful is better than ugly.
... Explicit is better than implicit.
... Simple is better than complex.
... Complex is better than complicated.
... Flat is better than nested.
... Sparse is better than dense."""

>>> markov(s)
'than ugly. Explicit is better than implicit. Simple is better than ugly. Explicit is better than nested. Sparse is better than complicated. '

'''
