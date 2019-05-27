import unittest


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        counts = [0] * 256

        for ch in s:
            counts[ord(ch)] += 1

        for ch in t:
            count = counts[ord(ch)]
            if not count:
                return False
            counts[ord(ch)] = count - 1

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('anagram', 'nagaram', True)
        self._test('rat', 'car', False)

    def _test(self, s, t, expected):
        actual = Solution().isAnagram(s, t)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
