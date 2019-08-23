import unittest

import utils


# O(n) time. O(1) space. Iteration, reverse.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        reversed_alpha_nums = (c.upper() for c in reversed(S) if c != '-')
        result = []

        for i, c in enumerate(reversed_alpha_nums):
            result.append(c)
            if (i + 1) % K == 0:
                result.append('-')

        if result and result[-1] == '-':
            result.pop()

        return ''.join(reversed(result))


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().licenseKeyFormatting(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
