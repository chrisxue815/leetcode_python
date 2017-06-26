import unittest


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            new_num = 0
            while num:
                num, r = divmod(num, 10)
                new_num += r
            num = new_num
        return num


class Test(unittest.TestCase):
    def test(self):
        self._test(38, 2)
        self._test(0, 0)

    def _test(self, num, expected):
        actual = Solution().addDigits(num)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
