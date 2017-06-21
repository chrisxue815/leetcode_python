import unittest


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = []
        while n:
            n, r = divmod(n - 1, 26)
            result.append(chr(r + ord('A')))
        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 'A')
        self._test(2, 'B')
        self._test(3, 'C')
        self._test(26, 'Z')
        self._test(27, 'AA')
        self._test(28, 'AB')

    def _test(self, n, expected):
        actual = Solution().convertToTitle(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
