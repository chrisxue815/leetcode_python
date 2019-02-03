import unittest


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        for i in range(len(nums)):
            hi = min(i + k + 1, len(nums))
            for j in range(i + 1, hi):
                if nums[i] == nums[j]:
                    return True
        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 3, 1, 5, 3], 3, True)
        self._test([4, 2, 3, 1, 5, 6], 3, False)

    def _test(self, nums, k, expected):
        actual = Solution().containsNearbyDuplicate(nums, k)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
