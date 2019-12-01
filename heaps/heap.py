def hprint(heap, width=None):
    if width is None:
        width = max(len(str(e)) for e in heap)
    height = int(log(len(heap), 2)) + 1
    gap = ' ' * width
    for h in range(height):
        below = 2 ** (height - h - 1)
        field = (2 * below - 1) * width
        print(gap.join(prepare(e, field) for e in level(heap, h)))


def max_heapify(A, i, n):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    if left < n and A[left] > A[largest]:
        largest = left
        
    if right < n and A[right] > A[largest]:
        largest = right

    if i != largest:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, largest, n)


def heap_sort(A):
    # Turn into heap
    for i in range(len(A), -1, -1):
        max_heapify(A, i, len(A))

    for i in range(len(A) - 1):
        A[0], A[len(A) - 1 - i] = A[len(A) - 1 - i], A[0]
        max_heapify(A, 0, len(A) - i - 1)
