import unittest


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counts = [0] * 32
        for num in nums:
            for i in range(32):
                counts[i] += (num >> i) & 1

        num = 0
        half_size = len(nums) >> 1
        for i in range(32):
            if counts[i] > half_size:
                num |= 1 << i

        if counts[31] > half_size:
            num |= -0x80000000

        return num


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 2], 2)
        self._test([-1], -1)

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
