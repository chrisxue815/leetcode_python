import unittest

import utils


# O(n) time. O(1) space. Recording indexes.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        curr_len = 0
        lo = 0
        indexes = [-1] * 128

        for hi, c in enumerate(s):
            c = ord(c)
            prev = indexes[c]
            if prev < lo:
                curr_len += 1
                result = max(result, curr_len)
            else:
                curr_len = hi - prev
                lo = prev
            indexes[c] = hi

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)
