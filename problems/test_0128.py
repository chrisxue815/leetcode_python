import unittest
import utils


# O(n) time. O(n) space. Hash table.
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        counts = {}

        for num in nums:
            if num in counts:
                continue

            lo = counts.get(num - 1, 0)
            hi = counts.get(num + 1, 0)

            count = lo + hi + 1
            if count > result:
                result = count

            counts[num] = count
            if lo:
                counts[num - lo] = count
            if hi:
                counts[num + hi] = count

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().longestConsecutive(**case.args._asdict())
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
