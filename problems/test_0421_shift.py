import unittest


class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(31, -1, -1):
            ret <<= 1
            prefixes = set(num >> i for num in nums)
            candidate = ret | 1
            ret += any(candidate ^ prefix in prefixes for prefix in prefixes)
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 10, 5, 25, 2, 8], 28)

    def _test(self, nums, expected):
        actual = Solution().findMaximumXOR(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
