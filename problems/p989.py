import unittest
import utils


# O(n) time. O(1) space. Algebra.
class Solution(object):
    def addToArrayForm(self, a, k):
        """
        :type a: List[int]
        :type k: int
        :rtype: List[int]
        """
        a.reverse()

        for i in xrange(len(a)):
            k, a[i] = divmod(a[i] + k, 10)

        while k > 0:
            k, r = divmod(k, 10)
            a.append(r)

        a.reverse()
        return a


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_json_from_path('../leetcode_test_cases/p989.json').test_cases

        for case in cases:
            actual = Solution().addToArrayForm(case.a, case.k)
            self.assertEqual(case.expected, actual)


if __name__ == '__main__':
    unittest.main()
