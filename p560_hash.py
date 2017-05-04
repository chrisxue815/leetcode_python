import collections
import unittest


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = collections.Counter()
        counter[0] = 1
        sum_ = 0
        count = 0

        for num in nums:
            sum_ += num
            count += counter[sum_ - k]
            counter[sum_] += 1
        return count


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 1], 2, 2)
        self._test([1, 2, 3, 4, 5], 5, 2)
        self._test([0, 0], 0, 3)

    def _test(self, nums, k, expected):
        actual = Solution().subarraySum(nums, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
