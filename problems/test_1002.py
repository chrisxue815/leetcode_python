import collections
import unittest
import utils


# O(n) time. O(1) space. Hash table.
class Solution:
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        counter = collections.Counter(A[0])

        for a in A:
            counter &= collections.Counter(a)

        return list(counter.elements())


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().commonChars(**case.args.__dict__)
            self.assertCountEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
