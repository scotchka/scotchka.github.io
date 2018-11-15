def merge(left, right):

    merged = []

    while left and right:
        if left[0] < right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))

    merged.extend(left)
    merged.extend(right)

    return merged


def mergesort(lst):

    queue = [[item] for item in lst]

    while len(queue) >= 2:
        left = queue.pop()
        right = queue.pop()
        merged = merge(left, right)
        queue.insert(0, merged)

    return queue[0]
