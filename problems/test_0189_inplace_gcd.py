import unittest


def gcd_euclid(a, b):
    if a == 0 or b == 0:
        return 0
    while b != 0:
        a, b = b, a % b
    return a


class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k %= n
        if k == 0:
            return
        if k < 0:
            k += n

        gcd = gcd_euclid(n, k)
        inner_loops = n / gcd

        for i in range(gcd):
            index = i
            prev = nums[index]
            for j in range(inner_loops):
                index = (index + k) % n
                nums[index], prev = prev, nums[index]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 10, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], -4, [5, 6, 7, 1, 2, 3, 4])
        self._test([1, 2, 3, 4, 5, 6, 7], 4, [4, 5, 6, 7, 1, 2, 3])

    def _test(self, nums, k, expected):
        Solution().rotate(nums, k)
        self.assertEqual(expected, nums)


if __name__ == '__main__':
    unittest.main()
