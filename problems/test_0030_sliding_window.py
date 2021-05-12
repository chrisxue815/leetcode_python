import collections
import unittest
from typing import List

import utils


# O(len(s) + len(words)) time. O(len(words)) space. Sliding window, hash table, queue.
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        result = []
        word_len = len(words[0])
        max_lo = len(s) - word_len * len(words)
        counts = collections.Counter(words)
        q = collections.deque()

        for lo in range(min(word_len, max_lo + 1)):
            while lo <= max_lo:
                hi = lo
                while True:
                    word = s[hi:hi + word_len]
                    if word not in counts:
                        lo = hi
                        break

                    while counts[word] == 0:
                        counts[q.popleft()] += 1
                        lo += word_len

                    q.append(word)
                    counts[word] -= 1
                    if len(q) == len(words):
                        result.append(lo)
                    hi += word_len

                while q:
                    counts[q.popleft()] += 1
                lo += word_len

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
