import unittest


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(len(findNums)):
            x = findNums[i]
            index = nums.index(x)
            for j in xrange(index + 1, len(nums)):
                if nums[j] > x:
                    findNums[i] = nums[j]
                    break
            else:
                findNums[i] = -1
        return findNums


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1])
        self._test([2, 4], [1, 2, 3, 4], [3, -1])

    def _test(self, findNums, nums, expected):
        actual = Solution().nextGreaterElement(findNums, nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
