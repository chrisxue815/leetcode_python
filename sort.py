import random
import unittest


# Insertion

def insertion_sort(a):
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
        self._test(bubble_sort)
        self._test(selection_sort)
        self._test(insertion_sort)
        self._test(binary_insertion_sort)
        self._test(shell_sort)
        self._test(quick_sort)

    def _test(self, func):
        unordered = list(self.unordered)
        func(unordered)
        self.assertEqual(unordered, self.ordered)


if __name__ == '__main__':
    unittest.main()
