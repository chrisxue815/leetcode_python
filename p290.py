import unittest


class Solution(object):
    def wordPattern(self, pattern, words):
        """
        :type pattern: str
        :type words: str
        :rtype: bool
        """
        words = words.split()
        if len(pattern) != len(words):
            return False
        ab = {}
        ba = {}
        for a, b in zip(pattern, words):
            a2 = ba.get(b, None)
            b2 = ab.get(a, None)
            if not a2 and not b2:
                ab[a] = b
                ba[b] = a
            elif a != a2 or b != b2:
                return False
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test('abba', 'dog cat cat dog', True)
        self._test('abba', 'dog cat cat fish', False)
        self._test('aaaa', 'dog cat cat dog', False)
        self._test('abba', 'dog dog dog dog', False)
        self._test('aaa', 'dog dog dog dog', False)

    def _test(self, pattern, words, expected):
        actual = Solution().wordPattern(pattern, words)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
