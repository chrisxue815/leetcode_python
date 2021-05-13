import unittest

import utils


# O(n) time. O(1) space. Two pointers.
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        result = 0

        for max_num_unique_chars in range(1, 27):
            counts = [0] * 128
            lo = 0
            hi = 0
            num_unique_chars = 0
            at_least_k = 0
            while hi < len(s):
                if num_unique_chars <= max_num_unique_chars:
                    c = ord(s[hi])
                    count = counts[c]
                    if count == 0:
                        num_unique_chars += 1
                    if count + 1 == k:
                        at_least_k += 1
                    counts[c] = count + 1
                    hi += 1
                else:
                    c = ord(s[lo])
                    count = counts[c]
                    if count == k:
                        at_least_k -= 1
                    if count == 1:
                        num_unique_chars -= 1
                    counts[c] = count - 1
                    lo += 1
                if num_unique_chars == max_num_unique_chars and num_unique_chars == at_least_k:
                    result = max(result, hi - lo)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
