import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def validMountainArray(self, a):
        """
        :type a: List[int]
        :rtype: bool
        """
        if len(a) < 3:
            return False

        i = 1

        while i < len(a) and a[i - 1] < a[i]:
            i += 1

        if i == 1 or i == len(a):
            return False

        while i < len(a) and a[i - 1] > a[i]:
            i += 1

        return i == len(a)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            actual = Solution().validMountainArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=case.args)


if __name__ == '__main__':
    unittest.main()
