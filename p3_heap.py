def max_heapify(a, i, heap_size, cnt):
    """Float a[i] down so subtree rooted at i is a max-heap.
    cnt is a one-element list used as a mutable comparison counter."""
    while True:
        l, r = 2 * i + 1, 2 * i + 2         # 0-indexed children
        largest = i
        if l < heap_size:
            cnt[0] += 1
            if a[l] > a[largest]:
                largest = l
        if r < heap_size:
            cnt[0] += 1
            if a[r] > a[largest]:
                largest = r
        if largest == i:
            return
        a[i], a[largest] = a[largest], a[i]
        i = largest


def build_max_heap(a, cnt):
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):     # last parent down to root
        max_heapify(a, i, n, cnt)


def heap_sort(arr):
    """Return (sorted_list, number_of_comparisons)."""
    a = arr[:]
    cnt = [0]
    build_max_heap(a, cnt)
    for end in range(len(a) - 1, 0, -1):
        a[0], a[end] = a[end], a[0]         # move current max to its final place
        max_heapify(a, 0, end, cnt)         # heap shrinks to a[0..end-1]
    return a, cnt[0]


if __name__ == "__main__":
    data = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    result, comps = heap_sort(data)
    print("Input     :", data)
    print("Sorted    :", result)
    print("Comparisons:", comps)
