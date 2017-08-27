import unittest


class Solution(object):
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 0

        for i in xrange(len(nums) - 1, 1, -1):
            side = nums[i]
            lo = 0
            hi = i - 1
            while lo < hi:
                if nums[lo] + nums[hi] > side:
                    result += hi - lo
                    hi -= 1
                else:
                    lo += 1

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 3, 4], 3)

    def _test(self, n, expected):
        actual = Solution().triangleNumber(n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
