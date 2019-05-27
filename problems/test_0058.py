import unittest


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        count = 0
        for ch in reversed(s):
            if ch != ' ':
                count += 1
            elif count:
                break
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test('Hello World', 5)
        self._test('World', 5)
        self._test('World  ', 5)
        self._test('', 0)
        self._test(None, 0)

    def _test(self, s, expected):
        actual = Solution().lengthOfLastWord(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
