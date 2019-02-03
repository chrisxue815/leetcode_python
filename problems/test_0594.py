import unittest
import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_len = 0
        counter = collections.Counter(nums)
        for num, count1 in list(counter.items()):
            count2 = counter[num + 1]
            if count2:
                length = count1 + count2
                if length > max_len:
                    max_len = length
        return max_len


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3, 2, 2, 5, 2, 3, 7], 5)

    def _test(self, wall, expected):
        actual = Solution().findLHS(wall)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
