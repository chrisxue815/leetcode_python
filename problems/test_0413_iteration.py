import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution:
    def numberOfArithmeticSlices(self, a):
        """
        :type a: List[int]
        :rtype: int
        """
        result = curr = 0
        for i in range(len(a) - 2):
            if a[i + 1] - a[i] == a[i + 2] - a[i + 1]:
                curr += 1
                result += curr
            else:
                curr = 0
        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().numberOfArithmeticSlices(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
