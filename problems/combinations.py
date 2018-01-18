import itertools
import unittest


def combinations_fix_elements(pool, r=None):
    r = len(pool) if r is None else r
    result = []
    _combinations_fix_elements(pool, r, result, [], 0)
    return result


def _combinations_fix_elements(pool, r, result, combination, start_index):
    if r == 0:
        result.append(tuple(combination))
    elif r > 0:
        for i in xrange(start_index, len(pool)):
            combination.append(pool[i])
            _combinations_fix_elements(pool, r - 1, result, combination, i + 1)
            combination.pop()


def combinations_include_exclude(pool, r=None):
    r = len(pool) if r is None else r
    result = []
    _combinations_include_exclude(pool, r, result, [], 0)
    return result


def _combinations_include_exclude(pool, r, result, combination, index):
    if r == 0:
        result.append(tuple(combination))
    elif r > 0 and index < len(pool):
        # include
        combination.append(pool[index])
        _combinations_include_exclude(pool, r - 1, result, combination, index + 1)
        combination.pop()

        # exclude
        _combinations_include_exclude(pool, r, result, combination, index + 1)


def combinations_iterative(pool, r=None):
    # See CPython:
    # https://docs.python.org/2/library/itertools.html#itertools.combinations
    # https://github.com/python/cpython/blob/bf623ae8843dc30b28c574bec8d29fc14be59d86/Modules/itertoolsmodule.c#L2465
    pool = tuple(pool)
    n = len(pool)
    if r is None:
        r = n
    elif r > n:
        return

    indices = range(r)
    yield tuple(pool[i] for i in indices)

    while True:
        # Find the last index
        for i in xrange(r - 1, -1, -1):
            # which is not the greatest possible at its position
            if indices[i] != n - r + i:
                break
        else:
            # Return if not found
            return

        indices[i] += 1
        for j in xrange(i + 1, r):
            indices[j] = indices[j - 1] + 1

        yield tuple(pool[i] for i in indices)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pools = [
            range(5),
        ]

    def test_combinations(self):
        self._test_combinations(combinations_fix_elements)
        self._test_combinations(combinations_include_exclude)
        self._test_combinations(combinations_iterative)

    def _test_combinations(self, func):
        for pool in Test.pools:
            for r in xrange(len(pool) + 2):
                actual = func(pool, r)
                expected = itertools.combinations(pool, r)
                self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
