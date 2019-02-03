import unittest
import math


# O(n) time. O(n) space. Bucket sort.
class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0

        min_ = min(nums)
        max_ = max(nums)

        if min_ == max_:
            return 0

        # Smallest possible maximum gap
        bucket_count = len(nums)
        bucket_size = int(math.ceil(float(max_ - min_) / (bucket_count - 1)))
        buckets = [None for _ in range(bucket_count)]

        for num in nums:
            index = (num - min_) // bucket_size
            bucket = buckets[index]
            if bucket:
                if num < bucket[0]:
                    bucket[0] = num
                if num > bucket[1]:
                    bucket[1] = num
            else:
                buckets[index] = [num, num]

        lo = 0
        for lo, bucket in enumerate(buckets):
            if bucket:
                break

        result = 0
        hi = lo + 1
        while True:
            while hi < bucket_count:
                if buckets[hi]:
                    break
                hi += 1
            else:
                break

            result = max(result, buckets[hi][0] - buckets[lo][1])
            lo, hi = hi, hi + 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 5, 6, 7, 0], 2)
        self._test([0, 1], 1)
        self._test([1, 1], 0)

    def _test(self, nums, expected):
        actual = Solution().maximumGap(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
