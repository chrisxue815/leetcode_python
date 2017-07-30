import unittest


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        counts = [0] * 256
        for ch in s:
            counts[ord(ch)] += 1
        for i, ch in enumerate(s):
            if counts[ord(ch)] == 1:
                return i
        return -1


class Test(unittest.TestCase):
    def test(self):
        self._test('leetcode', 0)
        self._test('loveleetcode', 2)

    def _test(self, s, expected):
        actual = Solution().firstUniqChar(s)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
