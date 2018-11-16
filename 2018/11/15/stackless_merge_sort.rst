Stackless merge sort
====================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

Merge sort divides a list into smaller lists of one or zero items, which
are trivially sorted, and then merges them pairwise until one list remains.
Here is a typical recursive implementation:

.. literalinclude:: msort.py
    :pyobject: mergesort

Note that the base case returns a copy, not the original list, to be
consistent with the general behavior. The ``merge`` function is:

.. literalinclude:: msort.py
    :pyobject: merge

For simplicity, we use `pop(0)` which is inefficient but easily remedied
with indexing.

Instead of dividing the list recursively, we can put each item into a list
by itself, and then merge them iteratively:

.. literalinclude:: msort.py
    :pyobject: mergesort_stackless

We maintain the individual lists in a queue. In each iteration, we take two lists from the queue,
merge them, and put the combined list back in the queue. Eventually just one list remains, which is
the desired result. The queue ensures that smaller lists are merged before larger ones, so that the
pair being merged does not become too different in size - unbalanced pairs would degrade runtime.

..
    >>> from msort import sort_stackless

Checking a test case:

>>> lst = [3, 2, 1, 4, 5]
>>> qsort_stackless(lst)
>>> lst
[1, 2, 3, 4, 5]
