import unittest

import utils


# O(n) time. O(1) space. String, DP.
class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        count = [0] * 26
        sub_len = 0

        for i, c in enumerate(p):
            if ord(p[i - 1]) + 1 == ord(c) or c == 'a' and p[i - 1] == 'z':
                sub_len += 1
            else:
                sub_len = 1

            index = ord(c) - ord('a')
            count[index] = max(count[index], sub_len)

        return sum(count)


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().findSubstringInWraproundString(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
