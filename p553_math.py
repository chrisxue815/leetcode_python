import unittest


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) == 1:
            return str(nums[0])
        elif len(nums) == 2:
            return str(nums[0]) + '/' + str(nums[1])

        return str(nums[0]) + '/(' + '/'.join(str(num) for num in nums[1:]) + ')'


class Test(unittest.TestCase):
    def test(self):
        self._test([1000, 100, 10, 2], '1000/(100/10/2)')

    def _test(self, nums, expected):
        actual = Solution().optimalDivision(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
