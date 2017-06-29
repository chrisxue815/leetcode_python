import unittest
import collections


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return collections.Counter(nums).most_common(1)[0][0]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 2], 2)

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
