import sys
import unittest


def _binary_search(a, x):
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = lo + ((hi - lo) >> 1)
        mid_val = a[mid]
        if mid_val < x:
            lo = mid + 1
        elif mid_val > x:
            hi = mid - 1
        else:
            return mid
    return lo


class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        max_radius = 0
        heaters.sort()

        for house in houses:
            heater_index = _binary_search(heaters, house)

            if heater_index < len(heaters):
                radius = heaters[heater_index] - house
            else:
                radius = sys.maxint

            if heater_index > 0:
                radius = min(radius, house - heaters[heater_index - 1])

            if max_radius < radius:
                max_radius = radius

        return max_radius


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], [2], 1)
        self._test([1, 2, 3, 4], [1, 4], 1)
        self._test([1], [1, 2, 3, 4], 0)
        self._test([1, 2], [1, 4], 1)
        self._test([1], [1, 2, 3, 4], 0)

    def _test(self, houses, heaters, expected):
        actual = Solution().findRadius(houses, heaters)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
