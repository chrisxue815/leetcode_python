import unittest


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        last = n - 1

        product = 1
        products = [1] * n
        for i in range(last):
            product *= nums[i]
            products[i + 1] = product

        product = 1
        for i in range(last, 0, -1):
            product *= nums[i]
            products[i - 1] *= product

        return products


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [24, 12, 8, 6])

    def _test(self, nums, expected):
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
