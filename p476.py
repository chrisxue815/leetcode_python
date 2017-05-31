import unittest


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        mask = num
        mask |= mask >> 1
        mask |= mask >> 2
        mask |= mask >> 4
        mask |= mask >> 8
        mask |= mask >> 16
        return num ^ mask


class Test(unittest.TestCase):
    def test(self):
        self._test(5, 2)
        self._test(1, 0)

    def _test(self, num, expected):
        actual = Solution().findComplement(num)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
