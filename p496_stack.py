import unittest


class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater = dict()
        stack = []

        for num in nums:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        for i in xrange(len(findNums)):
            findNums[i] = next_greater.get(findNums[i]) or -1

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
