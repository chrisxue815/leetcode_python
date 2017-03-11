import random
import unittest


# Insert

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


# Swap

def bubble_sort(a):
    n = len(a)
    for i in xrange(n):
        for j in xrange(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]


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

        n = 100
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

    def _test(self, func):
        unordered = list(self.unordered)
        func(unordered)
        self.assertEqual(unordered, self.ordered)


if __name__ == '__main__':
    unittest.main()
