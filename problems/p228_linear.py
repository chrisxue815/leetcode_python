import unittest


# O(n). Linear iteration
class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []

        result = []
        end = len(nums) - 1
        lo = nums[0]

        for i, hi in enumerate(nums):
            if i == end or hi + 1 != nums[i + 1]:
                if hi == lo:
                    result.append(str(lo))
                else:
                    result.append(str(lo) + '->' + str(hi))
                if i != end:
                    lo = nums[i + 1]

        return result


class Test(unittest.TestCase):
    def test(self):
        self._test([0, 1, 2, 4, 5, 7], ['0->2', '4->5', '7'])
        self._test([0, 2, 3, 4, 6, 8, 9], ['0', '2->4', '6', '8->9'])

    def _test(self, nums, expected):
        actual = Solution().summaryRanges(nums)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
