import unittest


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_ring = 0
        for index in xrange(len(nums)):
            ring = 0
            while True:
                num = nums[index]
                if num == -1:
                    break
                ring += 1
                nums[index] = -1
                index = num
            if ring > max_ring:
                max_ring = ring
        return max_ring


class Test(unittest.TestCase):
    def test(self):
        self._test([5, 4, 0, 3, 1, 6, 2], 4)

    def _test(self, nums, expected):
        actual = Solution().arrayNesting(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
