Why is an omnivore a kind of vegetarian?
========================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

An important principle in object oriented design is that you can replace an object of one class with another object
of its subclass, and the code should still work. For example, suppose we are creating a calorie counter for various
foods. We have a parent class

.. literalinclude:: liskov.py
    :pyobject: Food

and child classes

.. literalinclude:: liskov.py
    :pyobject: Vegetable

and

.. literalinclude:: liskov.py
    :pyobject: Meat

Consider a function that returns the calories of an item of food:

.. literalinclude:: liskov.py
    :pyobject: get_calories

Because a child class inherits the methods and attributes from its parent class -
possibly overriding some and adding others - any code that expects ``Food`` will
also work with ``Vegetable`` and ``Meat``.

..
    >>> from liskov import Food, Vegetable, Meat, get_calories, Omnivore, Vegetarian, Carnivore

>>> get_calories(Food('gruel', 1))
1
>>> get_calories(Vegetable('potato', 100))
100
>>> get_calories(Meat('steak', 500))
500

This ability to replace with a subclass is known as the "Liskov Substitution Principle".

Now let's turn to the consumers of food. Here is a possible class hierarchy:

.. literalinclude:: liskov.py
    :pyobject: Omnivore

.. literalinclude:: liskov.py
    :pyobject: Vegetarian

.. literalinclude:: liskov.py
    :pyobject: Carnivore

``Vegetarian`` and ``Carnivore`` override the ``eat`` method of ``Omnivore`` to raise an exception when
fed an argument that violates their respective dietary restrictions. An omnivore can consume both ``Vegetable``
and ``Meat``:

>>> guest = Omnivore()
>>> guest.eat(Vegetable('potato'))
potato YUM!
>>> guest.eat(Meat('steak'))
steak YUM!

But a vegetarian cannot consume ``Meat``:

>>> guest = Vegetarian()
>>> guest.eat(Vegetable('potato'))
potato YUM!
>>> guest.eat(Meat('steak'))
Traceback (most recent call last):
...
Exception: steak EWW

..
    >>> Carnivore().eat(Meat('steak'))
    steak YUM!
    >>> Carnivore().eat(Food('gruel'))
    Traceback (most recent call last):
    ...
    Exception: gruel EWW

The code breaks when an ``Omnivore`` is replaced by a ``Vegetarian``. Therefore, the
Liskov Substitution Principle implies, perhaps counterintuitively, that ``Vegetarian``
is not a subclass of ``Omnivore``.

This dilemma is resolved by observing that a ``Vegetarian`` can be replaced by an ``Omnivore``,
and hence the class hierarchy should be inverted - ``Omnivore`` being a subclass of ``Vegetarian``.
Of course, we can repeat the argument for ``Carnivore``, so ``Omnivore`` inherits from both
``Vegetarian`` and ``Carnivore``:

.. literalinclude:: contravariant.py
    :pyobject: Vegetarian

.. literalinclude:: contravariant.py
    :pyobject: Carnivore

.. literalinclude:: contravariant.py
    :pyobject: Omnivore

The key difference here is that, instead of raising an error, ``Vegetarian`` and ``Carnivore`` pass
the call to ``eat`` up the inheritance chain, hoping that another class is able to accept
the kind of food. The implementation of ``Omnivore`` is now trivial and intuitive - nothing more than the union of the consumers of ``Vegetable`` and ``Meat``.

..
    >>> from contravariant import Vegetarian, Carnivore, Omnivore

>>> guest = Vegetarian()
>>> guest.eat(Vegetable('potato'))
potato YUM!

>>> guest = Omnivore()
>>> guest.eat(Vegetable('potato'))
potato YUM!

>>> guest = Carnivore()
>>> guest.eat(Meat('steak'))
steak YUM!

>>> guest = Omnivore()
>>> guest.eat(Meat('steak'))
steak YUM!

..
    >>> Carnivore().eat(Vegetable('potato'))
    Traceback (most recent call last):
    ...
    AttributeError: 'super' object has no attribute 'eat'

We see that a ``Vegetarian`` or ``Carnivore`` can be replaced by an ``Omnivore``, so
our class hierarchy obeys Liskov Substitution. This example also illustrates a general rule:
a method of the child class should accept an argument that is less restrictive
(or not more restrictive) than the
corresponding method of the parent class. An ``Omnivore`` can eat either ``Vegetable`` or ``Meat``,
whereas a ``Vegetarian`` or ``Carnivore`` can only eat one of the food classes. In other words,
even though a child class is more specific than its parent, the child's methods take arguments
that are more general. This property of arguments is known as "contravariance".
