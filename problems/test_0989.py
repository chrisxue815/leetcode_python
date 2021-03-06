import unittest
import utils


# O(n) time. O(1) space. Algebra.
class Solution:
    def addToArrayForm(self, a, k):
        """
        :type a: List[int]
        :type k: int
        :rtype: List[int]
        """
        a.reverse()

        for i in range(len(a)):
            k, a[i] = divmod(a[i] + k, 10)

        while k > 0:
            k, r = divmod(k, 10)
            a.append(r)

        a.reverse()
        return a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().addToArrayForm(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
