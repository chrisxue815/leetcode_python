import unittest


class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        result = []
        for i in xrange(8):
            if num == 0:
                break
            digit = num & 15
            if digit < 10:
                result.append(chr(digit + ord('0')))
            else:
                result.append(chr(digit - 10 + ord('a')))
            num >>= 4
        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        self._test(26, '1a')
        self._test(-1, 'ffffffff')

    def _test(self, num, expected):
        actual = Solution().toHex(num)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
