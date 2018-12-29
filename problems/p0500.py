import unittest


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rows = [0] * ord('a') + [3, 4, 4, 3, 2, 3, 3, 3, 2, 3, 3, 3, 4, 4, 2, 2, 2, 2, 3, 2, 2, 4, 2, 4, 2, 4]
        ret = []
        for word in words:
            if word:
                word_lower = word.lower()
                row = rows[ord(word_lower[0])]
                if all(rows[ord(ch)] == row for ch in word_lower):
                    ret.append(word)
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test(['Hello', 'Alaska', 'Dad', 'Peace'], ['Alaska', 'Dad'])

    def _test(self, words, expected):
        actual = Solution().findWords(words)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
