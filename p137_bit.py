import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        bit0 = 0
        bit1 = 0
        for num in nums:
            bit0 = (bit0 ^ num) & ~bit1
            bit1 = (bit1 ^ num) & ~bit0
        return bit0


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 3, 3, 1, 5, 5, 5], 1)
        self._test([3, 5, 3, 5, 1, 3, 5], 1)

    def _test(self, nums, expected):
        actual = Solution().singleNumber(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
