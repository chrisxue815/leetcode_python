import unittest


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xorsum = 0
        for num in nums:
            xorsum ^= num

        xorsum &= -xorsum

        result = [0, 0]

        for num in nums:
            if num & xorsum:
                result[0] ^= num
            else:
                result[1] ^= num

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 1, 3, 2, 5], [3, 5])

    def _test(self, nums, expected):
        actual = Solution().singleNumber(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
