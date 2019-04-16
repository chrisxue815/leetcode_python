import unittest
import utils


# O(n) time. O(1) space. Kadane's algorithm, greedy.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_sum = nums[0]
        cur_sum = max_sum

        for num in nums[1:]:
            if cur_sum <= 0:
                cur_sum = num
            else:
                cur_sum += num

            if cur_sum > max_sum:
                max_sum = cur_sum

        return max_sum


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().maxSubArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
