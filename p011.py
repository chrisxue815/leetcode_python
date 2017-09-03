import unittest


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        max_area = 0

        while lo < hi:
            max_area = max(max_area, min(height[lo], height[hi]) * (hi - lo))
            if height[lo] < height[hi]:
                lo += 1
            else:
                hi -= 1

        return max_area


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 1, 0, 4], 8)
        self._test([2, 3, 1, 0, 4], 9)

    def _test(self, input, expected):
        actual = Solution().maxArea(input)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
