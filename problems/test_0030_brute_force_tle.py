import unittest
import collections


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        indices = []
        sub_len = len(words[0])
        total_len = sub_len * len(words)
        words = collections.Counter(words)

        for i in range(len(s) - total_len + 1):
            pending = words.copy()
            for j in range(i, i + total_len, sub_len):
                sub = s[j:j + sub_len]
                if pending[sub] == 0:
                    break
                pending[sub] -= 1
            else:
                indices.append(i)
        return indices


class Test(unittest.TestCase):
    def test(self):
        self._test('barfoothefoobarman', ['foo', 'bar'], [0, 9])
        self._test('wordgoodgoodgoodbestword', ["word", "good", "best", "good"], [8])

    def _test(self, s, words, expected):
        actual = Solution().findSubstring(s, words)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
