import random
import unittest


# Insertion

def insertion_sort(a):
    # see OpenJDK
    # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/8u40-b25/java/util/Arrays.java#1345
    n = len(a)
    for i in xrange(1, n):
        for j in xrange(i, 0, -1):
            if a[j - 1] <= a[j]:
                break
            a[j - 1], a[j] = a[j], a[j - 1]


def insertion_sort_memmove(a):
    n = len(a)
    for i in xrange(1, n):
        to_be_inserted = a[i]
        inserted = False
        for j in xrange(i - 1, -1, -1):
            if a[j] <= to_be_inserted:
                # memmove(a + j + 1, a + j, i - j)
                a[j + 2: i + 1] = a[j + 1: i]
                a[j + 1] = to_be_inserted
                inserted = True
                break
        if not inserted:
            a[1: i + 1] = a[0: i]
            a[0] = to_be_inserted


def binary_insertion_sort(a):
    n = len(a)
    for i in xrange(1, n):
        to_be_inserted = a[i]
        left = 0
        right = i - 1
        while left < right:
            middle = left + (right - left) // 2
            if to_be_inserted < a[middle]:
                right = middle - 1
            else:
                left = middle + 1
        if to_be_inserted < a[left]:
            a[left + 1: i + 1] = a[left: i]
            a[left] = to_be_inserted
        else:
            a[left + 2: i + 1] = a[left + 1: i]
            a[left + 1] = to_be_inserted


def _shell_gaps(n):
    gap = n // 2
    while gap > 0:
        yield gap
        gap //= 2


def shell_sort(a):
    n = len(a)
    for gap in _shell_gaps(n):
        for i in xrange(gap, n):
            to_be_inserted = a[i]
            j = i
            while j >= gap and a[j - gap] > to_be_inserted:
                a[j] = a[j - gap]
                j -= gap
            a[j] = to_be_inserted


# Swap

def bubble_sort(a):
    n = len(a)
    for i in xrange(n):
        for j in xrange(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


def _quick_sort(a, left, right):
    if left >= right:
        return
    middle = left + (right - left) // 2
    pivot = a[middle]
    i = left
    j = right
    while i <= j:
        while a[i] < pivot:
            i += 1
        while a[j] > pivot:
            j -= 1
        if i > j:
            break
        elif i < j:
            a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    # Optimization: tail call
    # see CLR
    # https://github.com/kasicass/sscli20/blob/dc64e12c9b835d4d373aa04978c0e8f1763b2e1b/clr/src/vm/comarrayhelpers.h#L77
    # https://github.com/kasicass/sscli20/blob/dc64e12c9b835d4d373aa04978c0e8f1763b2e1b/clr/src/bcl/system/collections/generic/arraysorthelper.cs#L70
    _quick_sort(a, left, j)
    _quick_sort(a, i, right)


def quick_sort(a):
    _quick_sort(a, 0, len(a) - 1)


# Selection

def selection_sort(a):
    n = len(a)
    for i in xrange(n):
        min_val = a[i]
        min_val_index = i
        for j in xrange(i + 1, n):
            if a[j] < min_val:
                min_val = a[j]
                min_val_index = j
        a[i], a[min_val_index] = a[min_val_index], a[i]


# Merging

def _merge_sort(dest, src, low, high):
    # Optimization: using insertion sort on smallest arrays (length < 7)
    # see OpenJDK
    # http://grepcode.com/file/repository.grepcode.com/java/root/jdk/openjdk/8u40-b25/java/util/Arrays.java#1338
    if low >= high - 1:
        return

    mid = low + (high - low) // 2
    _merge_sort(src, dest, low, mid)
    _merge_sort(src, dest, mid, high)

    if src[mid - 1] < src[mid]:
        dest[low: high] = src[low: high]
        return

    p = low
    q = mid
    for i in xrange(low, high):
        if q >= high or p < mid and src[p] < src[q]:
            dest[i] = src[p]
            p += 1
        else:
            dest[i] = src[q]
            q += 1


def merge_sort(a):
    aux = list(a)
    _merge_sort(a, aux, 0, len(a))


# Misc

def _heapify(a, root, n):
    left = 2 * root + 1
    right = 2 * root + 2
    largest = root

    if left < n and a[left] > a[largest]:
        largest = left
    if right < n and a[right] > a[largest]:
        largest = right

    if largest != root:
        a[largest], a[root] = a[root], a[largest]
        _heapify(a, largest, n)


def heap_sort(a):
    n = len(a)

    for i in xrange(n // 2 - 1, -1, -1):
        _heapify(a, i, n)

    for i in xrange(n - 1, -1, -1):
        a[0], a[i] = a[i], a[0]
        _heapify(a, 0, i)


class Test(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Test, self).__init__(*args, **kwargs)

        n = 10
        self.ordered = list(xrange(n))

        cloned = list(self.ordered)
        random_func = random.Random(1).random
        random.shuffle(cloned, random_func)
        self.unordered = cloned

    def test(self):
        self._test(insertion_sort)
        self._test(insertion_sort_memmove)
        self._test(binary_insertion_sort)
        self._test(shell_sort)
        self._test(bubble_sort)
        self._test(quick_sort)
        self._test(selection_sort)
        self._test(merge_sort)
        self._test(heap_sort)

    def _test(self, func):
        unordered = list(self.unordered)
        func(unordered)
        self.assertEqual(unordered, self.ordered)


if __name__ == '__main__':
    unittest.main()
