import unittest


class Solution:
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        was_space = True
        count = 0

        for ch in s:
            if ch != ' ':
                if was_space:
                    count += 1
                was_space = False
            else:
                was_space = True

        return count


class Test(unittest.TestCase):
    def test(self):
        self._test('Hello, my name is John', 5)
        self._test('  Hello, my  name is  John  ', 5)

    def _test(self, s, expected):
        actual = Solution().countSegments(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
