import unittest


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        return (num - 1) % 9 + 1 if num else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(38, 2)
        self._test(0, 0)

    def _test(self, num, expected):
        actual = Solution().addDigits(num)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
