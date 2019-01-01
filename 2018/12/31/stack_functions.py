def make_node(value, next_node):
    return lambda func: func(value, next_node)


def value(node):
    return node(lambda value, next_node: value)


def next_node(node):
    return node(lambda value, next_node: next_node)


def push(value, stack):
    return make_node(value, stack)


def pop(stack):
    return value(stack), next_node(stack)
