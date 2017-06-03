import unittest


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        num_ones = [0] * 32

        for num in nums:
            for i in xrange(32):
                if num == 0:
                    break
                if num & 1:
                    num_ones[i] += 1
                num >>= 1

        distance = 0
        for count in num_ones:
            distance += count * (n - count)

        return distance


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 14, 2], 6)

    def _test(self, nums, expected):
        actual = Solution().totalHammingDistance(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
