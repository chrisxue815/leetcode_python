import unittest


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        l = len(word)
        if l == 1:
            return True

        is_uppercase = word[1] <= 'Z'

        if word[0] > 'Z' and is_uppercase:
            return False

        for c in word[2:]:
            if (c <= 'Z') != is_uppercase:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('USA', True)
        self._test('leetcode', True)
        self._test('Google', True)
        self._test('a', True)
        self._test('A', True)
        self._test('USa', False)
        self._test('uSA', False)

    def _test(self, word, expected):
        self.assertEqual(expected, Solution().detectCapitalUse(word))


if __name__ == '__main__':
    unittest.main()
