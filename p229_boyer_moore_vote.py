import unittest


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        major1 = 0
        major2 = 1
        count1 = count2 = 0

        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
            elif not count1:
                major1 = num
                count1 = 1
            elif not count2:
                major2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        return [num for num in (major1, major2) if nums.count(num) > len(nums) // 3]


class Test(unittest.TestCase):
    def test(self):
        self._test([1, 1, 2], [1])
        self._test([1, 1, 1, 2], [1])
        self._test([1, 1, 1, 2, 2], [1, 2])
        self._test([1, 1, 1, 2, 2, 2], [1, 2])
        self._test([1, 1, 1, 2, 2, 2, 3], [1, 2])
        self._test([1, 1, 1, 2, 2, 2, 3, 3], [1, 2])
        self._test([1, 1, 1, 2, 2, 2, 3, 3, 3], [])
        self._test([-1], [-1])
        self._test([1, 2, 1, 3], [1])

    def _test(self, nums, expected):
        actual = Solution().majorityElement(nums)
        self.assertItemsEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
