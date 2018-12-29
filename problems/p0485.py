import unittest


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_count = 0
        count = 0

        for num in nums:
            if num == 1:
                count += 1
            else:
                if max_count < count:
                    max_count = count
                count = 0

        return max(max_count, count)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 0, 1, 1, 1], 3)

    def _test(self, nums, expected):
        actual = Solution().findMaxConsecutiveOnes(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
