import collections
import unittest
from typing import List

import utils


# O(len(s) * len(s) / len(word[0])) time.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        indices = []
        word_len = len(words[0])
        total_len = word_len * len(words)
        counts = collections.Counter(words)

        for i in range(len(s) - total_len + 1):
            pending = counts.copy()
            for j in range(i, i + total_len, word_len):
                word = s[j:j + word_len]
                if pending[word] == 0:
                    break
                pending[word] -= 1
            else:
                indices.append(i)
        return indices


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
