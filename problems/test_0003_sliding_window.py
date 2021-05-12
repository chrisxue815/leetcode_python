import unittest

import utils


# O(n) time. O(1) space. Sliding window.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        lo = 0
        counts = [0] * 128

        for hi, hi_char in enumerate(s):
            hi_char = ord(hi_char)

            if counts[hi_char] == 0:
                counts[hi_char] = 1
            else:
                result = max(result, hi - lo)
                while True:
                    lo_char = ord(s[lo])
                    lo += 1
                    if lo_char == hi_char:
                        break
                    else:
                        counts[lo_char] = 0

        return max(result, len(s) - lo)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
