import unittest


# O(n) time. O(1) space.
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i, num in enumerate(nums):
            while i != num - 1:
                i = num - 1
                num, nums[i] = nums[i], num

        result = []
        for i, num in enumerate(nums):
            if i != num - 1:
                result.append(i + 1)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])
        self._test([4, 3, 2, 7, 7, 2, 3, 1], [5, 6, 8])

    def _test(self, nums, expected):
        actual = Solution().findDisappearedNumbers(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
