import unittest


class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        for rank, (i, num) in enumerate(sorted(enumerate(nums), reverse=True, key=lambda x: x[1])):
            if rank > 2:
                nums[i] = str(rank + 1)
            elif rank == 0:
                nums[i] = 'Gold Medal'
            elif rank == 1:
                nums[i] = 'Silver Medal'
            elif rank == 2:
                nums[i] = 'Bronze Medal'
        return nums


class Test(unittest.TestCase):
    def test(self):
        self._test(
            [5, 4, 3, 2, 1],
            ['Gold Medal', 'Silver Medal', 'Bronze Medal', '4', '5']
        )

    def _test(self, nums, expected):
        actual = Solution().findRelativeRanks(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
