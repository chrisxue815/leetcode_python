import unittest

import utils


# O(n) time. O(1) space. Space-optimized stack.
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        result = 0
        curr = 0

        for c in S:
            if c == '(':
                curr += 1
            else:
                if curr == 0:
                    result += 1
                else:
                    curr -= 1

        return result + curr


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().minAddToMakeValid(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
