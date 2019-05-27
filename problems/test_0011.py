import unittest


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(height) - 1
        lo_height = height[lo]
        hi_height = height[hi]
        max_area = min(lo_height, hi_height) * (hi - lo)

        while lo < hi:
            if lo_height <= hi_height:
                lo += 1
                is_higher = height[lo] > lo_height
                lo_height = height[lo]
                if is_higher:
                    max_area = max(max_area, min(lo_height, hi_height) * (hi - lo))
            else:
                hi -= 1
                is_higher = height[hi] > hi_height
                hi_height = height[hi]
                if is_higher:
                    max_area = max(max_area, min(lo_height, hi_height) * (hi - lo))

        return max_area


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 2, 1, 0, 4], 8)
        self._test([2, 3, 1, 0, 4], 9)

    def _test(self, input, expected):
        actual = Solution().maxArea(input)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
