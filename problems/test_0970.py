import unittest
import utils


# O(log_x^{bound} * log_y^{bound}) time. O(log_x^{bound} * log_y^{bound}) space. Hash table.
class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = set()

        term1 = 1
        while term1 + 1 <= bound:

            term2 = 1
            while term1 + term2 <= bound:

                result.add(term1 + term2)

                if y == 1:
                    break

                term2 *= y

            if x == 1:
                break

            term1 *= x

        return list(result)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().powerfulIntegers(**case.args._asdict())
            self.assertCountEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
