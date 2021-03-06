import unittest


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pending = set()
        for num in nums:
            if num in pending:
                pending.remove(num)
            else:
                pending.add(num)
        return list(pending)


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 1, 3, 2, 5], [3, 5])

    def _test(self, nums, expected):
        actual = Solution().singleNumber(nums)
        self.assertCountEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
