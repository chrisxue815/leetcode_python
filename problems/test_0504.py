import unittest


class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        result = []
        tmp = abs(num)
        while tmp:
            tmp, r = divmod(tmp, 7)
            result.append(str(r))
        if num < 0:
            result.append('-')
        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        self._test(100, '202')
        self._test(-7, '-10')
        self._test(0, '0')

    def _test(self, num, expected):
        actual = Solution().convertToBase7(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
