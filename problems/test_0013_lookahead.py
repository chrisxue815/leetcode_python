import unittest

import utils

_SYMBOLS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# O(n) time. O(1) space. String.
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        for i in range(len(s) - 1):
            curr = _SYMBOLS[s[i]]
            if curr < _SYMBOLS[s[i + 1]]:
                result -= curr
            else:
                result += curr

        return result + _SYMBOLS[s[-1]]


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().romanToInt(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
