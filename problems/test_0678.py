import unittest


# O(n) time. O(1) space.
class Solution:
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lo = hi = 0
        for ch in s:
            if ch == '(':
                hi += 1
                lo += 1
            elif ch == ')':
                if hi == 0:
                    return False
                hi -= 1
                if lo > 0:
                    lo -= 1
            else:
                hi += 1
                if lo > 0:
                    lo -= 1
        return lo == 0


class Test(unittest.TestCase):
    def test(self):
        self._test('()', True)
        self._test('(*)', True)
        self._test('(*))', True)
        self._test('(*()', True)
        self._test('*', True)
        self._test('**', True)
        self._test('())*', False)

    def _test(self, s, expected):
        actual = Solution().checkValidString(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
