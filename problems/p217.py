import unittest


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        visited = set()
        for num in nums:
            if num in visited:
                return True
            visited.add(num)
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], False)
        self._test([1, 2, 3, 4, 3], True)

    def _test(self, nums, expected):
        actual = Solution().containsDuplicate(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
