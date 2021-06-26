import unittest
from typing import List

import utils


# O(nlog(n)) time. O(n) space. Binary search.
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        last_item_in_sequence = []
        for num in nums:
            lo = 0
            hi = len(last_item_in_sequence) - 1
            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_val = last_item_in_sequence[mid]
                if mid_val < num:
                    lo = mid + 1
                elif mid_val > num:
                    hi = mid - 1
                else:
                    lo = mid
                    break
            if lo == len(last_item_in_sequence):
                last_item_in_sequence.append(num)
            else:
                last_item_in_sequence[lo] = num
        return len(last_item_in_sequence)


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
