import unittest


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        max_ = 0
        stack = []
        for i in range(n):
            height = heights[i]
            left_index = i
            while stack and stack[-1][0] >= height:
                left_height, left_index = stack.pop()
                area = left_height * (i - left_index)
                if area > max_:
                    max_ = area
            stack.append((height, left_index))
        for height, index in stack:
            area = height * (n - index)
            if area > max_:
                max_ = area

        return max_


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 1, 5, 6, 2, 3], 10)
        self._test([1], 1)
        self._test([2, 1, 2], 3)

    def _test(self, heights, expected):
        actual = Solution().largestRectangleArea(heights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
