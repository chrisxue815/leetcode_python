import unittest


def is_beautiful(index, num):
    if index == num:
        return True
    elif index > num:
        return index % num == 0
    else:
        return num % index == 0


class Solution:
    def __init__(self):
        self.n = 0
        self.count = 0

    def countArrangement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.n = n
        self._count(list(range(1, n + 1)), n - 1)
        return self.count

    def _count(self, nums, start):
        if start == -1:
            self.count += 1
        else:
            next_index = start - 1
            index = start + 1
            if is_beautiful(index, nums[start]):
                self._count(nums, next_index)

            for i in range(next_index, -1, -1):
                if is_beautiful(index, nums[i]):
                    nums[i], nums[start] = nums[start], nums[i]
                    self._count(nums, next_index)
                    nums[i], nums[start] = nums[start], nums[i]


class Test(unittest.TestCase):
    def test(self):
        self._test(1, 1)
        self._test(2, 2)
        self._test(3, 3)
        self._test(7, 41)

    def _test(self, n, expected):
        actual = Solution().countArrangement(n)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
