import unittest

import utils


# O(n) time. O(1) space. Iteration, reverse.
class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        result = []

        for c in reversed(S):
            if c != '-':
                if len(result) % (K + 1) == K:
                    result.append('-')
                result.append(c.upper())

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
