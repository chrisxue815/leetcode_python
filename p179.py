import unittest


def cmp_concat_result(x, y):
    for a, b in zip(x, y):
        if a < b:
            return -1
        elif a > b:
            return 1

    if len(x) == len(y):
        return 0

    if len(x) < len(y):
        x = y[len(x):] + x
    else:
        y = x[len(y):] + y

    for a, b in zip(x, y):
        if a < b:
            return 1
        elif a > b:
            return -1
    return 0


# O(nlog(n)). Sorting
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]

        nums.sort(cmp=cmp_concat_result, reverse=True)

        result = ''.join(nums).lstrip('0')
        return result if result else '0'


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 30, 34, 5, 9], '9534330')
        self._test([3, 30, 34, 5, 9, 91], '991534330')
        self._test([0, 0], '0')

    def _test(self, nums, expected):
        actual = Solution().largestNumber(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
