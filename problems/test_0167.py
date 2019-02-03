import unittest


def _index_of(a, x, lo, hi):
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < x:
            lo = mid + 1
        elif a[mid] > x:
            hi = mid - 1
        else:
            return mid

    return -1


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(numbers)
        for i in range(n):
            x = target - numbers[i]
            j = _index_of(numbers, x, i + 1, n - 1)
            if j != -1:
                return [i + 1, j + 1]


class Test(unittest.TestCase):
    def test(self):
        self._test([2, 7, 11, 15], 9, [1, 2])
        self._test([-5, -2, 7, 11, 15], 9, [2, 4])

    def _test(self, numbers, target, expected):
        actual = Solution().twoSum(numbers, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
