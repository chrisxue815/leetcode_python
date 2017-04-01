import unittest


class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        visited = set()
        for num in nums[:k + 1]:
            if num in visited:
                return True
            visited.add(num)

        for i in xrange(k + 1, len(nums)):
            visited.remove(nums[i - k - 1])
            if nums[i] in visited:
                return True
            visited.add(nums[i])

        return False


class Test(unittest.TestCase):
    def test(self):
        self._test([4, 2, 3, 1, 5, 3], 3, True)
        self._test([4, 2, 3, 1, 5, 6], 3, False)

    def _test(self, nums, k, expected):
        actual = Solution().containsNearbyDuplicate(nums, k)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
