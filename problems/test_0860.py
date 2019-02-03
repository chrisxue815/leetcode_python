import unittest
import utils


# O(n) time. O(1) space. Greedy.
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        bills_5 = bills_10 = bills_20 = 0

        for bill in bills:
            if bill == 5:
                bills_5 += 1
            elif bill == 10:
                if bills_5 >= 1:
                    bills_5 -= 1
                    bills_10 += 1
                else:
                    return False
            else:
                if bills_5 >= 1 and bills_10 >= 1:
                    bills_5 -= 1
                    bills_10 -= 1
                    bills_20 += 1
                elif bills_5 >= 3:
                    bills_5 -= 3
                    bills_20 += 1
                else:
                    return False

        return True


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().lemonadeChange(**case.args._asdict())
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
