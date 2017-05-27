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
        word_len = len(words[0])
        total_len = word_len * len(words)
        words = collections.Counter(words)

        for lo in xrange(word_len):
            curr = lo

            while True:
                hi = lo + total_len
                if hi > len(s):
                    break

                if lo == curr:
                    pending = words.copy()

                while curr < hi:
                    word = s[curr:curr + word_len]
                    num_pending = pending[word]

                    if num_pending > 0:
                        pending[word] = num_pending - 1
                    elif words[word] == 0:
                        curr += word_len
                        lo = curr
                        break
                    else:
                        while True:
                            deleting_sub = s[lo:lo + word_len]
                            lo += word_len
                            if deleting_sub == word:
                                break
                            pending[deleting_sub] += 1
                        hi = lo + total_len
                        if hi > len(s):
                            break
                    curr += word_len
                else:
                    indices.append(lo)
                    pending[s[lo:lo + word_len]] += 1
                    lo += word_len

        return indices


class Test(unittest.TestCase):
    def test(self):
        self._test('barfoofoobarthefoobarman', ["bar", "foo", "the"], [6, 9, 12])
        self._test('barfoothefoobarman', ['foo', 'bar'], [0, 9])
        self._test('wordgoodgoodgoodbestword', ["word", "good", "best", "good"], [8])

    def _test(self, s, words, expected):
        actual = Solution().findSubstring(s, words)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
