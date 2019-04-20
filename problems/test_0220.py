import unittest
from typing import List

import utils


# O(n) time. O(k) space. Bucket.
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k <= 0 or t < 0:
            return False

        size = t + 1
        buckets = {}

        for i, num in enumerate(nums):
            bucket = num // size

            if bucket in buckets:
                return True

            left = buckets.get(bucket - 1)
            if left is not None and num - left <= t:
                return True

            right = buckets.get(bucket + 1)
            if right is not None and right - num <= t:
                return True

            if len(buckets) >= k:
                del buckets[nums[i - k] // size]
            buckets[bucket] = num

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().containsNearbyAlmostDuplicate(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
