import collections
import unittest


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0 or not nums:
            return 0

        counter = collections.Counter()

        for num in nums:
            counter[num] += 1

        num_pairs = 0
        if k == 0:
            for num, count in counter.items():
                if count >= 2:
                    num_pairs += 1
        else:
            for num in counter:
                if counter[num + k] > 0:
                    num_pairs += 1

        return num_pairs


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 1, 4, 1, 5], 2, 2)
        self._test([1, 2, 3, 4, 5], 1, 4)
        self._test([1, 3, 1, 5, 4], 0, 1)
        self._test([1, 3, 1, 5, 4], -1, 0)

    def _test(self, nums, k, expected):
        actual = Solution().findPairs(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
