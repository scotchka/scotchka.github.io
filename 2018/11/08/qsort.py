def qsort_recursive(lst, start=0, end=None):
    if end is None:
        end = len(lst)

    if end - start < 2:
        return

    pivot_position = partition(lst, start, end)

    qsort_recursive(lst, start, pivot_position)
    qsort_recursive(lst, pivot_position + 1, end)


def qsort_stackless(lst):
    not_sorted = {(0, len(lst))}

    while not_sorted:
        start, end = not_sorted.pop()

        pivot_position = partition(lst, start, end)

        if pivot_position - start > 0:
            not_sorted.add((start, pivot_position))

        if end - (pivot_position + 1) > 0:
            not_sorted.add((pivot_position + 1, end))


def partition(lst, start, end):
    pivot = lst[start]
    rest = lst[start + 1 : end]

    left = [item for item in rest if item <= pivot]
    right = [item for item in rest if item > pivot]

    lst[start:end] = left + [pivot] + right

    return start + len(left)
