import unittest


class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for num in nums:
            if num == 0:
                continue

            i = num - 1
            next_i = nums[i] - 1
            while next_i > -1:
                nums[i] = 0
                i = next_i
                next_i = nums[i] - 1

        result = []
        for i in xrange(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 3, 2, 7, 8, 2, 3, 1], [5, 6])
        self._test([4, 3, 2, 7, 7, 2, 3, 1], [5, 6, 8])

    def _test(self, nums, expected):
        actual = Solution().findDisappearedNumbers(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
