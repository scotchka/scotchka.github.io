Why is an omnivore a kind of vegetarian?
========================================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

An important principle in object oriented design is that you can replace an object of one type with another object
of its subtype, and the code should still work. For example, suppose we are creating a calorie counter for various
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
    >>> from liskov import Food, Vegetable, Meat, get_calories

>>> get_calories(Food('gruel', 1))
1
>>> get_calories(Vegetable('potato', 100))
100
>>> get_calories(Meat('steak', 500))
500

