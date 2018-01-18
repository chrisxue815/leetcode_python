import unittest
import sys


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ak = -sys.maxint - 1
        stack = []
        for num in reversed(nums):
            if num < ak:
                return True
            while stack and num > stack[-1]:
                ak = stack.pop()
            stack.append(num)
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], False)
        self._test([3, 1, 4, 2], True)
        self._test([-1, 3, 2, 0], True)
        self._test([3, 1, 4, 0], False)
        self._test([3, 1, 4, 0, 5], False)
        self._test([3, 1, 4, 0, 5, 3], True)
        self._test([3, 1, 2], False)
        self._test([4, 1, 3, 2], True)
        self._test([8, 10, 4, 6, 5], True)
        self._test([3, 5, 0, 3, 4], True)

    def _test(self, nums, expected):
        actual = Solution().find132pattern(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
