import unittest


# O(n). Math
class Solution:
    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        result = list(range(1, n - k))

        for i in range(k + 1):
            if i & 1:
                result.append(n - (i >> 1))
            else:
                result.append(n - k + (i >> 1))

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(3, 1, [1, 2, 3])
        self._test(3, 2, [1, 3, 2])

    def _test(self, n, k, expected):
        actual = Solution().constructArray(n, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
