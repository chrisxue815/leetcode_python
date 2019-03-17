import unittest


class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        # See CPython itertools.combinations():
        # https://docs.python.org/2/library/itertools.html#itertools.combinations
        # https://github.com/python/cpython/blob/bf623ae8843dc30b28c574bec8d29fc14be59d86/Modules/itertoolsmodule.c#L2465
        result = []
        combination = list(range(1, k + 1))
        result.append(list(combination))

        while True:
            # Find the last index
            for i in range(k - 1, -1, -1):
                # which is not the greatest possible at its position
                if combination[i] != n - k + i + 1:
                    break
            else:
                # Return if not found
                return result

            combination[i] += 1
            for j in range(i + 1, k):
                combination[j] = combination[j - 1] + 1

            result.append(list(combination))


class Test(unittest.TestCase):
    def test(self):
        self._test(4, 2, [
            [2, 4],
            [3, 4],
            [2, 3],
            [1, 2],
            [1, 3],
            [1, 4],
        ])

    def _test(self, n, k, expected):
        actual = Solution().combine(n, k)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
