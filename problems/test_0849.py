import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        lo = 0

        while lo < len(seats) and seats[lo] == 0:
            lo += 1

        result = lo

        for hi in range(lo + 1, len(seats)):
            if seats[hi] == 1:
                if seats[hi - 1] == 0:
                    result = max(result, (hi - lo) >> 1)
                lo = hi

        result = max(result, len(seats) - lo - 1)

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().maxDistToClosest(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
