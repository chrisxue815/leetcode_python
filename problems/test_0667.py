import unittest

from typing import List

import utils


# O(n) time. O(1) space. Math.
class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        result = list(range(1, n - k))

        for i in range(k + 1):
            if i & 1:
                result.append(n - (i >> 1))
            else:
                result.append(n - k + (i >> 1))

        return result


class Test(unittest.TestCase):
    def test(self):
        cases = utils.load_test_json(__file__).test_cases

        for case in cases:
            args = str(case.args)
            actual = Solution().constructArray(**case.args.__dict__)
            self.assertEqual(case.expected, actual, msg=args)


if __name__ == '__main__':
    unittest.main()
