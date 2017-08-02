import unittest


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pending = set(xrange(1, len(nums) + 1))
        result = [0] * 2
        for num in nums:
            if num in pending:
                pending.remove(num)
            else:
                result[0] = num
        result[1] = next(iter(pending))
        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 4], [2, 3])

    def _test(self, nums, expected):
        actual = Solution().findErrorNums(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
