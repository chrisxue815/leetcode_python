import unittest


class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        prev_end = 0
        total = 0

        for time in timeSeries:
            if time < prev_end:
                new_end = time + duration
                total += new_end - prev_end
                prev_end = new_end
            else:
                total += duration
                prev_end = time + duration

        return total


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 4], 2, 4)
        self._test([1, 2], 2, 3)

    def _test(self, timeSeries, duration, expected):
        actual = Solution().findPoisonedDuration(timeSeries, duration)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
