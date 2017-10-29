import unittest


# O(n) time. O(1) space. Greedy.
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        result = 0
        miss = 1
        i = 0
        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                miss <<= 1
                result += 1
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 3], 6, 1)
        self._test([1, 5, 10], 20, 2)
        self._test([1, 2, 2], 5, 0)

    def _test(self, nums, n, expected):
        actual = Solution().minPatches(nums, n)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
