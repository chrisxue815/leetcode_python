import unittest


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = mask = 0
        for i in xrange(31, -1, -1):
            mask |= 1 << i
            prefixes = set()
            for num in nums:
                prefixes.add(num & mask)
            tmp = ret | (1 << i)
            for prefix in prefixes:
                if tmp ^ prefix in prefixes:
                    ret = tmp
                    break
        return ret


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 10, 5, 25, 2, 8], 28)

    def _test(self, nums, expected):
        actual = Solution().findMaximumXOR(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
