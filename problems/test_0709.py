import unittest
import utils


# O(n) time. O(1) space. Iteration.
class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        return ''.join(chr(ord(ch) - ord('A') + ord('a')) if ord('A') <= ord(ch) <= ord('Z') else ch for ch in str)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().toLowerCase(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
