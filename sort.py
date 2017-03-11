import random
import unittest


def bubble_sort(a):
    n = len(a)
    for i in xrange(n):
        for j in xrange(1, n - i):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
    return a


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

    def _test(self, func):
        unordered = list(self.unordered)
        self.assertEqual(func(unordered), self.ordered)


if __name__ == '__main__':
    unittest.main()
