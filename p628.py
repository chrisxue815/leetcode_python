import unittest
import heapq
import operator


def prod(iterable):
    return reduce(operator.mul, iterable, 1)


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos = [0] * 3
        neg = [0] * 3
        zero = 0
        for num in nums:
            if num > 0:
                heapq.heappushpop(pos, num)
            elif num < 0:
                heapq._heappushpop_max(neg, num)
            else:
                zero = 1
        pos = sorted(num for num in pos if num)
        neg = sorted(num for num in neg if num)
        if len(pos) >= 3:
            if len(neg) >= 2:
                if pos[0] * pos[1] >= neg[0] * neg[1]:
                    return pos[0] * pos[1] * pos[2]
                else:
                    return pos[2] * neg[0] * neg[1]
            else:
                return pos[0] * pos[1] * pos[2]
        elif len(pos) == 2:
            if len(neg) >= 2:
                return pos[1] * neg[0] * neg[1]
            else:
                return 0 if zero else pos[0] * pos[1] * neg[0]
        elif len(pos) == 1:
            if len(neg) >= 2:
                return pos[0] * neg[0] * neg[1]
            else:
                return 0
        else:
            return 0 if zero else prod(heapq.nlargest(3, nums))


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3], 6)
        self._test([1, 2, 3, 4], 24)
        self._test([1, 2, 3, -4, -5], 60)
        self._test([1, 2, 3, -4], 6)
        self._test([1, 2, -3, -4], 24)
        self._test([1, 2, -3, 0], 0)
        self._test([1, 2, -3], -6)
        self._test([1, -2, -3, -4], 12)
        self._test([1, -2, 0], 0)
        self._test([1, 0, 0], 0)
        self._test([-1, -2, -3, 0], 0)
        self._test([-1, -2, -3, -4], -6)

    def _test(self, nums, expected):
        actual = Solution().maximumProduct(nums)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
