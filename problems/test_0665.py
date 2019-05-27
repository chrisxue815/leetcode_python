import unittest


# O(n) time. O(1) space.
class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        allow_mod = True
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i + 1]:
                continue

            if not allow_mod:
                return False

            allow_mod = False

            if i < 1 or nums[i - 1] <= nums[i + 1]:
                continue

            if i + 2 >= len(nums) or nums[i] <= nums[i + 2]:
                nums[i + 1] = nums[i]
                continue

            return False
        return True


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 3], True)
        self._test([4, 2, 1], False)

    def _test(self, nums, expected):
        actual = Solution().checkPossibility(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
