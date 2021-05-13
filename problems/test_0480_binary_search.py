import bisect
import unittest
from typing import List

import utils


# O(nlog(n)) time. O(k) space. Binary search.
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        half = k >> 1
        window = sorted(nums[:k])
        result = [float(window[half]) if k & 1 else (window[half - 1] + window[half]) / 2]

        for hi in range(k, len(nums)):
            bisect.insort(window, nums[hi])
            lo_window_index = bisect.bisect_left(window, nums[hi - k])
            window.pop(lo_window_index)
            result.append(float(window[half]) if k & 1 else (window[half - 1] + window[half]) / 2)

        return result


class Test(unittest.TestCase):
    def test(self):
        utils.test(self, __file__, Solution)


if __name__ == '__main__':
    unittest.main()
