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
    else:
        for i in xrange(start_index, len(pool)):
            combination.append(pool[i])
            _combinations_fix_elements(pool, r - 1, result, combination, i + 1)
            combination.pop()


def permutations_dummy(pool, r=None):
    return itertools.permutations(pool, r)


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pools = [
            range(3),
        ]

        cls.combination_funcs = [
            combinations_fix_elements,
        ]

        cls.permutation_funcs = [
            permutations_dummy,
        ]

    def test_combinations(self):
        for pool in Test.pools:
            for r in xrange(len(pool) + 1):
                expected = itertools.combinations(pool, r)
                for func in Test.combination_funcs:
                    actual = func(pool, r)
                    self.assertItemsEqual(actual, expected)

    def test_permutations(self):
        for pool in Test.pools:
            for r in xrange(len(pool) + 1):
                expected = itertools.permutations(pool, r)
                for func in Test.permutation_funcs:
                    actual = func(pool, r)
                    self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
