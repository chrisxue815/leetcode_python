import unittest


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = 0
        for i in range(32):
            mask = 1 << i
            count = 0
            for num in nums:
                if num & mask:
                    count += 1
            total += count * (n - count)
        return total


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 14, 2], 6)

    def _test(self, nums, expected):
        actual = Solution().totalHammingDistance(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
