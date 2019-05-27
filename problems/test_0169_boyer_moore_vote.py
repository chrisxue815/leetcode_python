import unittest


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = count = 0

        for num in nums:
            if num == major:
                count += 1
            elif count > 0:
                count -= 1
            else:
                major = num
                count = 1
        return major


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 2, 2, 2], 2)
        self._test([1, 2, 2, 2, 1], 2)
        self._test([-1], -1)

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
