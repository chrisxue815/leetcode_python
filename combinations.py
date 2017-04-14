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


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pools = [
            range(3),
        ]

    def test_combinations(self):
        self._test_combinations(combinations_fix_elements)
        self._test_combinations(combinations_include_exclude)

    def _test_combinations(self, func):
        for pool in Test.pools:
            for r in xrange(len(pool) + 2):
                actual = func(pool, r)
                expected = itertools.combinations(pool, r)
                self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
