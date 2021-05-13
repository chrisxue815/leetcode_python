import collections
import unittest

import utils


# O(n) time. O(n) space. Recursion.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        counts = collections.Counter(s)
        for c, count in counts.items():
            if count < k:
                return max(self.longestSubstring(sub, k) for sub in s.split(c))

        return len(s)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
