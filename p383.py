import unittest


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        magazine_char_counts = [0] * 256
        for ch in magazine:
            magazine_char_counts[ord(ch)] += 1

        for ch in ransomNote:
            count = magazine_char_counts[ord(ch)]
            if count <= 0:
                return False
            magazine_char_counts[ord(ch)] = count - 1

        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('a', 'b', False)
        self._test('aa', 'ab', False)
        self._test('aa', 'aab', True)

    def _test(self, ransomNote, magazine, expected):
        actual = Solution().canConstruct(ransomNote, magazine)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
