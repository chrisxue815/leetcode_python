import unittest


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)

        product = 1
        left_products = [1]
        for num in nums:
            product *= num
            left_products.append(product)

        product = 1
        right_products = [1]
        for num in reversed(nums):
            product *= num
            right_products.append(product)

        products = []
        last = n - 1
        for i in range(n):
            left = left_products[i]
            right = right_products[last - i]
            products.append(left * right)

        return products


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 3, 4], [24, 12, 8, 6])

    def _test(self, nums, expected):
        actual = Solution().productExceptSelf(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
