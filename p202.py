import unittest


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = set()
        while n not in visited:
            visited.add(n)
            sq_sum = 0
            while n:
                n, r = divmod(n, 10)
                sq_sum += r * r
            if sq_sum == 1:
                return True
            n = sq_sum
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test(19, True)
        self._test(7, True)

    def _test(self, n, expected):
        actual = Solution().isHappy(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
