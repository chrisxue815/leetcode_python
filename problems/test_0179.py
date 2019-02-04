import functools
import unittest


def cmp(a, b):
    return (a > b) - (a < b)


# O(nlog(n)). Sorting
class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        nums = [str(num) for num in nums]

        nums.sort(key=functools.cmp_to_key(lambda x, y: cmp(y + x, x + y)))

        result = ''.join(nums).lstrip('0')
        return result if result else '0'


class Test(unittest.TestCase):
    def test(self):
        self._test([3, 30, 34, 5, 9], '9534330')
        self._test([3, 30, 34, 5, 9, 91], '991534330')
        self._test([0, 0], '0')

    def _test(self, nums, expected):
        actual = Solution().largestNumber(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
