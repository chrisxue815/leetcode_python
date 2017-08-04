import unittest


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        max_s = s = sum(nums[:k])
        for i, num in enumerate(nums[k:]):
            s += num - nums[i]
            if s > max_s:
                max_s = s
        return float(max_s) / k


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 12, -5, -6, 50, 3], 4, 12.75)

    def _test(self, nums, k, expected):
        actual = Solution().findMaxAverage(nums, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
