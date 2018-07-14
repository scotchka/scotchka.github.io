"""
>>> from tree import Node, traverse_recursive, traverse_iterative, traverse_tail_recursive

>>> tree = Node.make_tree([1, 2, 3, 4, 5, 6])

>>> traverse_recursive(tree)
1
2
3
4
5
6

>>> traverse_iterative(tree)
1
2
3
4
5
6

>>> traverse_tail_recursive(
...     [
...         (tree, "right"), 
...         (tree, "left")
...     ]
... )
1
2
3
4
5
6

"""
