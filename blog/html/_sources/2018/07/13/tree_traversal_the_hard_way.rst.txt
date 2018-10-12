Tree traversal made hard
========================



.. author:: default
.. categories:: none
.. tags:: none
.. comments::

Tree traversal is a well known task for which recursion is simple and natural. We define a Node
class.

.. literalinclude:: tree.py
    :pyobject: Node

The class method ``make_tree`` returns the root node of a balanced binary tree from a list of values.
If the list is sorted, then the tree is a binary search tree (BST). A BST has the important property
that if you do an in-order traversal of the nodes, you will visit them in order.
A recursive implementation of in-order traversal is straightforward.

.. literalinclude:: tree.py
    :pyobject: traverse_recursive

Let's test it with a small sorted list of integers and verify that the nodes are printed out in order.

.. literalinclude:: test_tree.txt
    :lines: 4-12

Now, what if we insist on traversing **without** recursion? In lieu of the call stack, we need to
maintain our own stack. Each item in our stack would hold the same information as a call frame.
In ``traverse_recursive`` there are two potential recursive calls, each call adding another frame to
the call stack. Since a recursive call suspends the calling frame, our stack must maintain a
state - whether or not the left side of the BST has been examined. Let's designate the possibilities
for this state ``"left"`` and ``"right"``.

.. literalinclude:: tree.py
    :pyobject: traverse_iterative

Each call frame becomes, in our stack, a pair of items - as the stack is popped off, the left side of
each node is examined before the right. The analogue of a recursive call is pushing another pair to the stack.
Let's test ``traverse_iterative`` on the same BST.

.. literalinclude:: test_tree.txt
    :lines: 14-20

Note that an in-order traversal is different from a depth-first search (DFS). To implement DFS iteratively,
we simply maintain a stack of nodes without the additional state. This is because DFS first checks whether
the target node has been found (and if so, exits) **before** adding the child nodes to the stack. Hence there
is no reason to "remember" the parent node. Formally, DFS on a binary tree is equivalent to a pre-order traversal.

The iterative implementation of in-order tree traversal is less intuitive than the recursive version, which nicely
illustrates that recursion is sometimes **much easier** than iteration. Though iteration has the advantage
of not growing the call stack, and readily leads to tail recursion.

.. literalinclude:: tree.py
    :pyobject: traverse_tail_recursive

Calling ``traverse_tail_recursive`` with the same tree but wrapped inside of a stack:

.. literalinclude:: test_tree.txt
    :lines: 22-33

Python does not offer tail call optimization, but in languages that do, this example suggests a recipe
for turning a recursive function into a tail recursive function: via an intermediate iterative implementation.
