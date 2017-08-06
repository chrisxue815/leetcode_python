import unittest


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        prev = nums[0]
        i = 1

        for i in xrange(i, len(nums)):
            curr = nums[i]
            if curr < prev:
                lo, hi, max_num, min_num = i - 1, i, prev, curr
                while lo >= 0 and nums[lo] > curr:
                    lo -= 1
                break
            prev = curr
        else:
            return 0

        while True:
            for i in xrange(i, len(nums)):
                curr = nums[i]
                if curr >= max_num:
                    hi = i - 1
                    prev = curr
                    i += 1
                    break
                elif curr < min_num:
                    while lo >= 0 and nums[lo] > curr:
                        lo -= 1
                    min_num = nums[lo]
            else:
                return len(nums) - 1 - lo

            for i in xrange(i, len(nums)):
                curr = nums[i]
                if curr < prev:
                    hi, max_num = i, prev
                    if curr < min_num:
                        min_num = curr
                        while lo >= 0 and nums[lo] > curr:
                            lo -= 1
                    break
                prev = curr
            else:
                return hi - lo


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 6, 4, 8, 10, 9, 15], 5)

    def _test(self, nums, expected):
        actual = Solution().findUnsortedSubarray(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
