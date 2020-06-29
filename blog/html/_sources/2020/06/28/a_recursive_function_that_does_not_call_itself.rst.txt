A recursive function that does not call itself
==============================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::


Consider the standard implementation of factorial:

>>> fact = lambda n: 1 if n < 2 else n * fact(n - 1)
>>> fact(5)
120

The ``lambda`` expression
creates anonymous or inline functions in Python. However, here
we are effectively naming the function by assigning it to the variable ``fact``.
This assignment is necessary because the function itself refers to ``fact``, which
means we cannot use this function inline.

If we insist on a truly anonymous version of factorial, it helps to think of
self-reference not as a defining feature of recursion, but an implementation
detail. It is merely a very convenient way to apply the same function on progressively
smaller inputs. Without self-reference, we need a different way to talk about
the same function. The trick is to create an enclosing scope and pass in the function itself:

>>> fact = lambda f: lambda n: 1 if n < 2 else n * f(f)(n - 1)

In the outer scope, ``f`` refers to ``fact``, and since it now has an outer scope,
``f(f)`` is the inner function, ie, the actual computation. Hence we have to call
``fact`` as follows:

>>> fact(fact)(5)
120

Having removed self-reference, we can replace ``fact`` with its
value to arrive at an inline factorial:

>>> (lambda f: lambda n: 1 if n < 2 else n * f(f)(n - 1))(
...     lambda f: lambda n: 1 if n < 2 else n * f(f)(n - 1)
... )(5)
120

While achieving the goal of a recursive function that does not call itself,
the above example contains two copies of the factorial logic and the awkward
``f(f)``.

Let's first remedy the latter problem by introducing a decorator function:

.. literalinclude:: y_combinator_simple.py

The decorator ``y_1`` allows us to write ``fact`` in a more natural way by
factoring out the "unwrapping" of the enclosing scope. As before,

..
	>>> from y_combinator_simple import fact

>>> fact(fact)(5)
120

It is straightfoward to eliminate the double reference by having the decorator
do the replication as well:

.. literalinclude:: y_combinator_final.py

``fact`` now works as a normal function should:

..
	>>> from y_combinator_final import fact, y_2

>>> fact(5)
120

Note that ``y_2`` has nothing to do with factorials (parameter names are arbitrary). To confirm this, let's apply it to a version of quicksort:

>>> y_2(
...     lambda f: lambda lst: []
...     if not lst  # base case
...     else f([n for n in lst[1:] if n < lst[0]])
...     + [lst[0]]
...     + f([n for n in lst[1:] if n >= lst[0]])
... )([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]
True

We see that ``y_2`` is part of a generic recipe to create recursive functions without self-reference. It is an implementation of the Y combinator, which
was invented in the context of the lambda calculus, a formal language that does not have variables - so every "program" is basically an inline function call.
Remarkably, the Y combinator shows that even such a minimal language is capable of
doing recursive computation.
