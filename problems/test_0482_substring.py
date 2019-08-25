import unittest

import utils


# O(n) time. O(n) space. Iteration, substring.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        alpha_nums = S.replace('-', '').upper()[::-1]
        return '-'.join(alpha_nums[i:i + K] for i in range(0, len(alpha_nums), K))[::-1]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().licenseKeyFormatting(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
