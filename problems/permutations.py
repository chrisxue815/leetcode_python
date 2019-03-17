import itertools
import unittest


def permutations_recursive(pool, r=None):
    pool = list(pool)
    n = len(pool)
    if r is None:
        r = n
    elif r > n:
        return []

    result = []
    _permutations_recursive(pool, r, result, 0)
    return result


def _permutations_recursive(pool, r, result, start_index):
    if start_index == r:
        result.append(tuple(pool[:r]))
    else:
        next_index = start_index + 1
        _permutations_recursive(pool, r, result, next_index)

        for i in range(next_index, len(pool)):
            pool[i], pool[start_index] = pool[start_index], pool[i]
            _permutations_recursive(pool, r, result, next_index)
            pool[i], pool[start_index] = pool[start_index], pool[i]


def permutations_iterative(pool, r=None):
    # See CPython itertools.permutations():
    # https://docs.python.org/2/library/itertools.html#itertools.permutations
    # https://github.com/python/cpython/blob/bf623ae8843dc30b28c574bec8d29fc14be59d86/Modules/itertoolsmodule.c#L3153
    pool = tuple(pool)
    n = len(pool)
    if r is None:
        r = n
    elif r > n:
        return

    indices = list(range(n))
    cycles = list(range(r))
    yield tuple(pool[i] for i in indices[:r])

    while True:
        # Find the last index
        for i in range(r - 1, -1, -1):
            cycles[i] += 1
            j = cycles[i]

            # which is not the greatest possible at its position
            if j < n:
                indices[i], indices[j] = indices[j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
            else:
                # Reset cycles[i]
                cycles[i] = i

                # Move indices[i] to the end
                indices[i:] = indices[i + 1:] + [indices[i]]
        else:
            return


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.pools = [
            list(range(5)),
        ]

    def test_permutations(self):
        self._test_permutations(permutations_recursive)
        self._test_permutations(permutations_iterative)

    def _test_permutations(self, func):
        for pool in Test.pools:
            for r in range(len(pool) + 2):
                actual = func(pool, r)
                expected = itertools.permutations(pool, r)
                self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
