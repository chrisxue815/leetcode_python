import unittest

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        sum_ = sum(A)
        target, r = divmod(sum_, 3)

        if r:
            return False

        target_reached = False
        s = 0

        for num in A:
            s += num

            if s == target:
                if target_reached:
                    return True
                else:
                    target_reached = True
                    s = 0

        return False


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().canThreePartsEqualSum(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
