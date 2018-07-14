class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return repr(self.value)

    @classmethod
    def make_tree(cls, values):
        if len(values) == 0:
            return None

        mid = len(values) // 2

        return Node(
            values[mid],
            left=cls.make_tree(values[:mid]),
            right=cls.make_tree(values[mid + 1 :]),
        )


def traverse_recursive(node):
    if node.left:
        traverse_recursive(node.left)

    print(node)

    if node.right:
        traverse_recursive(node.right)


def traverse_iterative(node):

    stack = []

    stack.append((node, "right"))
    stack.append((node, "left"))

    while stack:
        node, state = stack.pop()
        if state == "left":
            if node.left:
                stack.append((node.left, "right"))
                stack.append((node.left, "left"))
        elif state == "right":
            print(node)
            if node.right:
                stack.append((node.right, "right"))
                stack.append((node.right, "left"))

        else:
            raise ValueError("unknown state")


def traverse_tail_recursive(stack):

    if not stack:
        return

    node, state = stack.pop()

    if state == "left":
        if node.left:
            stack.append((node.left, "right"))
            stack.append((node.left, "left"))
    elif state == "right":
        print(node)
        if node.right:
            stack.append((node.right, "right"))
            stack.append((node.right, "left"))

    else:
        raise ValueError("unknown state")

    traverse_tail_recursive(stack)
