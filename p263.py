import unittest


class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        for factor in [5, 3, 2]:
            while True:
                q, r = divmod(num, factor)
                if r:
                    break
                num = q
        return num == 1


class Test(unittest.TestCase):
    def test(self):
        self._test(1, True)
        self._test(2, True)
        self._test(3, True)
        self._test(4, True)
        self._test(5, True)
        self._test(6, True)
        self._test(7, False)
        self._test(8, True)
        self._test(9, True)
        self._test(10, True)
        self._test(11, False)
        self._test(12, True)
        self._test(13, False)
        self._test(14, False)

    def _test(self, n, expected):
        actual = Solution().isUgly(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
