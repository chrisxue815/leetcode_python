import unittest

import utils

_SYMBOLS = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}


# O(n) time. O(1) space. String.
class Solution:
    def romanToInt(self, s: str) -> int:
        result = prev = 0

        for ch in reversed(s):
            curr = _SYMBOLS[ch]
            if curr < prev:
                result -= curr
            else:
                result += curr
            prev = curr

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().romanToInt(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
