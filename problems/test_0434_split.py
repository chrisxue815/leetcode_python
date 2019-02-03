import unittest


class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())


class Test(unittest.TestCase):
    def test(self):
        self._test('Hello, my name is John', 5)
        self._test('  Hello, my  name is  John  ', 5)

    def _test(self, s, expected):
        actual = Solution().countSegments(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
