import unittest
from typing import List

import utils


# O(n) time. O(1) space. Two pointers, greedy.
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []

        result = []
        lo = 0
        lo_ch = ord(s[0])
        rightmost_index = [-1] * (ord('z') + 1)

        for hi in range(len(s) - 1, -1, -1):
            hi_ch = ord(s[hi])
            if rightmost_index[hi_ch] == -1:
                rightmost_index[hi_ch] = hi

            if hi_ch == lo_ch:
                break

        while lo < len(s):
            hi = rightmost_index[ord(s[lo])]
            i = lo

            while i < hi:
                ch = ord(s[i])
                rightmost = rightmost_index[ch]
                if rightmost > hi:
                    hi = rightmost
                i += 1

            result.append(hi - lo + 1)
            lo = hi + 1

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
