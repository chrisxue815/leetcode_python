import unittest


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        result = len(nums) + 1
        sums = [0] * len(nums)  # itertools.accumulate
        sum_ = 0

        for i, num in enumerate(nums):
            sum_ += num
            sums[i] = sum_

        for end, end_sum in enumerate(sums):
            lo = 0
            hi = end

            while lo <= hi:
                mid = lo + ((hi - lo) >> 1)
                mid_sum = sums[mid]

                if end_sum - mid_sum >= s:
                    lo = mid + 1
                else:
                    hi = mid - 1

            if end_sum - sums[hi] >= s:
                result = min(result, end - hi)
            elif end_sum >= s:
                result = min(result, end + 1)

        return result if result != len(nums) + 1 else 0


class Test(unittest.TestCase):
    def test(self):
        self._test(7, [2, 3, 1, 2, 4, 3], 2)
        self._test(15, [1, 2, 3, 4, 5], 5)

    def _test(self, s, nums, expected):
        actual = Solution().minSubArrayLen(s, nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
