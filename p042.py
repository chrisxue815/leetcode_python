import unittest


class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left = 0
        right = len(heights) - 1
        left_peak = 0
        right_peak = 0
        water = 0

        while left < right:
            left_height = heights[left]
            right_height = heights[right]
            if left_height <= right_height:
                if left_height >= left_peak:
                    left_peak = left_height
                else:
                    water += left_peak - left_height
                left += 1
            else:
                if right_height >= right_peak:
                    right_peak = right_height
                else:
                    water += right_peak - right_height
                right -= 1

        return water


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
        self._test([0, 4, 0, 3, 0, 2, 0, 1, 0, 2, 0, 3, 0, 4, 0], 33)

    def _test(self, heights, expected):
        actual = Solution().trap(heights)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
