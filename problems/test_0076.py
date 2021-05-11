import unittest

import utils


# O(n) time. O(1) space. Counting, sliding window.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = [0] * 128
        for c in t:
            counts[ord(c)] -= 1

        result_length = 0x7FFFFFFF
        result_lo = 0
        result_hi = 0
        lo = 0
        pending = sum(1 for count in counts if count < 0)

        for hi, c in enumerate(s):
            counts[ord(c)] += 1
            if counts[ord(c)] == 0:
                pending -= 1

            while lo <= hi and counts[ord(s[lo])] > 0:
                counts[ord(s[lo])] -= 1
                lo += 1

            if pending == 0 and result_length > hi - lo:
                result_length = hi - lo
                result_lo = lo
                result_hi = hi + 1

        return s[result_lo:result_hi]


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)
