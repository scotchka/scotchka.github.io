'''
>>> lst = [1, 2, 3]
>>> lst.append(lst)
>>> lst
[1, 2, 3, [...]]
>>> lst[-1] is lst
True

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

'''
