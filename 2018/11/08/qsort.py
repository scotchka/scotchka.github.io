def qsort_recursive(lst, start=0, end=None):
    if end is None:
        end = len(lst)

    if end - start < 2:
        return

    pivot = lst[start]
    rest = lst[start + 1:end]

    left = [item for item in rest if item <= pivot]
    right = [item for item in rest if item > pivot]

    lst[start:end] = left + [pivot] + right

    qsort_recursive(lst, start, start + len(left))
    qsort_recursive(lst, end - len(right), end)



def qsort_stackless(lst):
    not_sorted = {(0, len(lst))}

    while not_sorted:
        start, end = not_sorted.pop()

        segment = lst[start:end]

        pivot = segment[0]
        rest = segment[1:]

        left = [item for item in rest if item <= pivot]
        right = [item for item in rest if item > pivot]

        lst[start:end] = left + [pivot] + right

        if len(left) > 0:
            not_sorted.add((start, start + len(left)))

        if len(right) > 0:
            not_sorted.add((end - len(right), end))