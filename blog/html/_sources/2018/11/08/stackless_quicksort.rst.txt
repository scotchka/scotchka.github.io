Stackless quicksort
===================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

Quicksort is a famous example of a recursive algorithm. Here is a sub-optimal
implementation:

.. literalinclude:: qsort.py
    :pyobject: qsort

The ``partition`` function chooses a pivot value and places it at the correct position, with smaller values
to its left and larger values to its right. It also returns the final position of the pivot value.

.. literalinclude:: qsort.py
    :pyobject: partition

For brevity, we use list slicing instead of swaps, but the discussion does not
depend on how the partitioning is done.

..
    >>> from qsort import qsort, qsort_stackless
    >>> lst = [3, 2, 1, 4, 5]
    >>> qsort(lst)
    >>> lst
    [1, 2, 3, 4, 5]

In the above implementation, observe that each recursive call stands alone, simply sorting a
segment of the list. As this `article <https://bertrandmeyer.com/2014/12/07/lampsort/>`_ points out,
the recursive call stack serves merely to ensure that the list is divided into smaller segments
until every item is a pivot or belongs to a segment of one item.

Because the order in which different parts of the list is sorted is immaterial, we don't need recursion
or even a stack for that matter. Here is an implementation of quicksort using a set to track which segments
are still to be sorted:

.. literalinclude:: qsort.py
    :pyobject: qsort_stackless

The set ``not_sorted`` contains start and end indices of segments which remain to be sorted. Note that
the ``pop`` method returns an **arbitrary** element of a set, which becomes empty when no unsorted segments
remain. The list is then sorted. Let's check a test case:

>>> lst = [3, 2, 1, 4, 5]
>>> qsort_stackless(lst)
>>> lst
[1, 2, 3, 4, 5]
