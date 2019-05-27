import unittest


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        write_index = 0
        for num in nums:
            if num != val:
                nums[write_index] = num
                write_index += 1
        return write_index


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 2, 2, 3], 3, [2, 2])

    def _test(self, nums, val, expected):
        actual = Solution().removeElement(nums, val)
        self.assertEqual(len(expected), actual)
        self.assertEqual(expected, nums[:actual])


if __name__ == '__main__':
    unittest.main()
