"""
>>> from tree import Node, traverse_recursive, traverse_iterative

>>> values = [1, 2, 3,4,5,6,7]
>>> tree = Node.make_tree(values)
>>> traverse_recursive(tree)
<1>
<2>
<3>
<4>
<5>
<6>
<7>

>>> traverse_iterative(tree)
<1>
<2>
<3>
<4>
<5>
<6>
<7>

"""
