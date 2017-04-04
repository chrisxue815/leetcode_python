import unittest


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []

        for i in xrange(len(nums)):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            for j in xrange(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j - 1] == nums[j]:
                    continue

                residual = target - nums[i] - nums[j]
                lo = j + 1
                hi = len(nums) - 1

                while lo < hi:
                    sum_ = nums[lo] + nums[hi]
                    if sum_ < residual:
                        lo += 1
                    elif sum_ > residual:
                        hi -= 1
                    else:
                        result.append([nums[i], nums[j], nums[lo], nums[hi]])
                        lo += 1
                        while lo < hi and nums[lo - 1] == nums[lo]:
                            lo += 1
                        hi -= 1
                        while lo < hi and nums[hi] == nums[hi + 1]:
                            hi -= 1
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [-2, -1, 0, 0, 1, 2],
            0,
            [
                [-1, 0, 0, 1],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2]
            ])

        self._test(
            [0, 0, 0, 0],
            0,
            [
                [0, 0, 0, 0],
            ])

    def _test(self, nums, target, expected):
        actual = Solution().fourSum(nums, target)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
