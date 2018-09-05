import unittest
import utils


# O(log(n)) time. O(1) space. Binary search.
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo = 0
        hi = len(nums) - 1

        while lo <= hi:
            mid = lo + ((hi - lo) >> 1)
            mid_val = nums[mid]

            if mid_val < target:
                lo = mid + 1
            elif mid_val > target:
                hi = mid - 1
            else:
                return mid

        return -1


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p704.json').test_cases

        for case in cases:
            actual = Solution().search(case.nums, case.target)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
