import unittest


def permutations(n):
    result = []
    _permutations(n, result, range(1, n + 1), 0)
    return result


def _permutations(n, result, p, start):
    if start == n:
        result.append(tuple(p))
    else:
        next_index = start + 1
        _permutations(n, result, p, next_index)

        for i in xrange(next_index, n):
            p[i], p[start] = p[start], p[i]
            _permutations(n, result, p, next_index)
            p[i], p[start] = p[start], p[i]


def is_beautiful(index, num):
    if index == num:
        return True
    elif index > num:
        return index % num == 0
    else:
        return num % index == 0


class Solution(object):
    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for permutation in permutations(n):
            for index, num in enumerate(permutation):
                if not is_beautiful(index + 1, num):
                    break
            else:
                count += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(2, 2)
        self._test(3, 3)
        self._test(7, 41)

    def _test(self, n, expected):
        actual = Solution().countArrangement(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
