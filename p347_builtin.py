import unittest
import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        return nums if k == len(nums) else [num for num, _ in collections.Counter(nums).most_common(k)]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 1, 2, 2, 3], 2, [1, 2])
        self._test([1], 1, [1])

    def _test(self, nums, k, expected):
        actual = Solution().topKFrequent(nums, k)
        self.assertItemsEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
