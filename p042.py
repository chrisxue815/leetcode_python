import unittest


class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0

        left_peaks = []
        curr_max = -1
        for i, height in enumerate(heights):
            if height > curr_max:
                curr_max = height
                left_peaks.append((i, height))

        right_peaks = []
        curr_max = -1
        for i in xrange(len(heights) - 1, -1, -1):
            height = heights[i]
            if height > curr_max:
                curr_max = height
                right_peaks.append((i, height))

        water = 0
        if len(left_peaks) > 1:
            peak_index = 1
            curr_peak_height = left_peaks[0][1]
            next_peak_index = left_peaks[1][0]
            for i, height in enumerate(heights):
                if i >= next_peak_index:
                    peak_index += 1
                    if peak_index >= len(left_peaks):
                        break
                    curr_peak_height = left_peaks[peak_index - 1][1]
                    next_peak_index = left_peaks[peak_index][0]
                water += curr_peak_height - height

        peak_index = len(right_peaks) - 1
        curr_peak_height = right_peaks[-1][1]
        next_peak_index = right_peaks[-1][0]
        for i in xrange(i + 1, len(heights)):
            height = heights[i]
            if i > next_peak_index:
                peak_index -= 1
                curr_peak_height = right_peaks[peak_index][1]
                next_peak_index = right_peaks[peak_index][0]
            water += curr_peak_height - height

        return water


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
        self._test([0, 4, 0, 3, 0, 2, 0, 1, 0, 2, 0, 3, 0, 4, 0], 33)

    def _test(self, heights, expected):
        actual = Solution().trap(heights)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
